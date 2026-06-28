from database.database import Database


from formatter import *

from cep import get_cep


from typing import Any


class Controller():
    def __init__(self):
        self.db = Database()

    def validate_text(self, text:str) -> bool:
        return is_valid_text(text)
    
    def validate_num(self, num:str) -> bool:
        return is_valid_num(num)

    def validate_cpf_cnpj(self, cpf_cnpj:str) -> bool:
        return is_valid_cpf_cnpj(cpf_cnpj)
    
    def validate_data_nascimento(self, data_nascimento:str) -> bool:
        return is_valid_data_nascimento(data_nascimento)
    
    def validate_contato(self, contato:str) -> bool:
        return is_valid_contato(contato)
    
    def validate_cep(self, cep:str) -> bool:
        return is_valid_cep(cep)

    def autocomplete_address(self, cep:str) -> dict[str, str]:

        address:dict[str, str] = {'valido': 'false'}

        if not is_valid_cep(cep):
            return address
        
        num_cep = format_num(cep)

        try:
            api_data = get_cep(num_cep)

            if 'erro' in api_data:
                return address
            
            address['valido'] = 'true'
            address['rua'] = api_data['logradouro']
            address['complemento'] = api_data['complemento']
            address['bairro'] = api_data['bairro']
            address['cidade'] = api_data['localidade']
            address['uf'] = api_data['uf']
            address['cep'] = api_data['cep']

            return address

        except Exception as e:
            print("Could not autocomplete address. Error:", e)

    def _format_data(self, nome:str, data_nascimento:str, cpf_cnpj:str, 
        contato:str, rua:str, numero:str, complemento:str, bairro:str, 
        cidade:str, uf:str, cep:str) -> dict[str, tuple]:

        data:dict[str, tuple] = {'provider': None, 'address': None}

        data['provider'] = (
            format_text(nome), 
            format_data_nascimento(data_nascimento), 
            format_cpf_cnpj(cpf_cnpj), 
            format_contato(contato)
        )

        data['address'] = (
            format_text(rua), 
            format_num(numero), 
            format_text(complemento),
            format_text(bairro), 
            format_text(cidade), 
            format_text(uf), 
            format_cep(cep)
        )

        return data

    # Suppose all entered data is valid
    def insert_db(self, nome:str, data_nascimento:str, cpf_cnpj:str, 
        contato:str, rua:str, numero:str, complemento:str, bairro:str, 
        cidade:str, uf:str, cep:str) -> None:
        
        data = self._format_data(
            nome, data_nascimento, cpf_cnpj, contato, rua, numero, complemento, 
            bairro, cidade, uf, cep
        )
        
        try:
            self.db.insert(data)

        except Exception as e:
            print("Could not insert to database. Error:", e)

    def verify_id(self, id:int):
        return self.db.verify_id(id)

    # Suppose the id exists in the database and all the data is valid
    def update_db(self, id:int, nome:str, data_nascimento:str, cpf_cnpj:str, 
        contato:str, rua:str, numero:str, complemento:str, bairro:str, 
        cidade:str, uf:str, cep:str) -> None:

        data = self._format_data(
            nome, data_nascimento, cpf_cnpj, contato, rua, numero, complemento, 
            bairro, cidade, uf, cep
        )

        try:
            self.db.update(id, data)

        except Exception as e:
            print("Could not update the database. Error:", e)

    # Suppose the id exists in the database
    def delete_db(self, id:int) -> None:
        
        try:
            self.db.delete(id)

        except Exception as e:
            print("Could not delete the data. Error:", e)

    # Suppose the id exists in the database
    def read_id(self, id:int) -> Any | None:

        try:
            return self.db.read_id(id)

        except Exception as e:
            print("Could not get the data. Error:", e)

    def read_db(self) -> list[Any] | None:
        
        try:
            return self.db.fetch()

        except Exception as e:
            print("Could not fetch the data. Error:", e)


# Example of usage
def main():
    controller = Controller()
    
    # Autocomplete address
    print(controller.autocomplete_address("01001000"))

    # Example of inserting
    nome = "Beltrano da Silva"
    data_nascimento = "12-12-2000"
    cpf_cnpj = "78951707083"
    contato = "12999999999"
    cep = "01001000"
    address = controller.autocomplete_address("01001000")
    rua = address['rua']
    numero = "01"
    complemento = address['complemento']
    bairro = address['bairro']
    cidade = address['cidade']
    uf = address['uf']

    controller.insert_db(nome, data_nascimento, cpf_cnpj, contato, rua, numero,
        complemento, bairro, cidade, uf, cep)
    
    # Read data from the database
    rows = controller.read_db()
    for row in rows:
        print(row)

    # Update an entry from the database
    id_up = 1
    contato_up = "+21 99999-9999"
    controller.update_db(id_up, None, None, None, contato_up, None, None, None, 
        None, None, None, None)
    
    # Read updated data from the database
    row_up = controller.read_id(id_up)
    print(row_up)

    # Delete an entry from the database
    id_del = 1
    controller.delete_db(id_del)

    # Read data from the database
    rows = controller.read_db()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()