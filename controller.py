from database.database import Database

from formatter import (
    format_num,
    format_text,
    is_valid_text,
    is_valid_num,
    is_valid_cpf_cnpj, 
    is_valid_data_nascimento,
    is_valid_contato,
    is_valid_cep
)

from cep import get_cep


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

    # Suppose all entered data is valid
    def insert_db(self, nome:str, data_nascimento:str, cpf_cnpj:str, 
        contato:str, rua:str, numero:str, complemento:str, bairro:str, 
        cidade:str, uf:str, cep:str) -> None:
        
        data:dict[str, tuple] = {'provider': None, 'address': None}

        data['provider'] = (
            format_text(nome), 
            format_num(data_nascimento), 
            format_num(cpf_cnpj), 
            format_num(contato)
        )

        if complemento is not None:
            complemento = format_text(complemento)

        data['address'] = (
            format_text(rua), 
            format_num(numero), 
            complemento,
            format_text(bairro), 
            format_text(cidade), 
            format_text(uf), 
            format_num(cep)
        )

        try:
            self.db.insert(data)

        except Exception as e:
            print("Could not insert to database. Error:", e)


# Example of usage
def main():
    controller = Controller()
    
    # Autocomplete address
    print(controller.autocomplete_address("01001000"))

    # Example of inserting
    nome = "Beltrano da Silva"
    data_nascimento = "12-12-2000"
    cpf_cnpj = "789.517.070-83"
    contato = "+12 99999-9999"
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


if __name__ == "__main__":
    main()