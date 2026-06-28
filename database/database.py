import sqlite3


DATABASE_PATH = './database/database.db'

class Database():
    def __init__(self):
        self.conn = None
        self._create()

    def _connect(self):
        try:
            self.conn = sqlite3.connect(DATABASE_PATH)
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to open database:", e)

    def _create(self):
        self._connect()
        
        try:
            sql_statements:list[str] = [
                """CREATE TABLE IF NOT EXISTS prestadores (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        data_nascimento TEXT NOT NULL,
                        cpf_cnpj TEXT NOT NULL,
                        contato TEXT NOT NULL
                    );""",
                """CREATE TABLE IF NOT EXISTS enderecos (
                        id_prestador INT NOT NULL,
                        rua TEXT NOT NULL,
                        numero TEXT NOT NULL, 
                        complemento TEXT,
                        bairro TEXT NOT NULL,
                        cidade TEXT NOT NULL,
                        uf TEXT NOT NULL,
                        cep TEXT NOT NULL,
                        FOREIGN KEY (id_prestador) REFERENCES prestadores (id)
                    );"""
            ]

            for statement in sql_statements:
                self.conn.execute(statement)

            self.conn.commit()
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to create tables:", e)

        finally:
            self.conn.close()

    def _insert_provider(self, provider:tuple):
        self._connect()

        try:
            statement:str = """INSERT INTO prestadores(
                nome,data_nascimento,cpf_cnpj,contato
            ) VALUES(?,?,?,?);"""
            
            cur = self.conn.cursor()

            cur.execute(statement, provider)

            self.conn.commit()

            return cur.lastrowid
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to insert provider:", e)

        finally:
            self.conn.close()

    def _insert_address(self, address:tuple):
        self._connect()

        try:
            statement:str = """INSERT INTO enderecos(
                id_prestador,rua,numero,complemento,bairro,cidade,uf,cep
            ) VALUES(?,?,?,?,?,?,?,?);"""
            
            cur = self.conn.cursor()

            cur.execute(statement, address)

            self.conn.commit()
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to insert address:", e)

        finally:
            self.conn.close()

    def insert(self, data: dict[str, tuple]):

        try:
            provider:tuple = data['provider']
            id_prestador:int = self._insert_provider(provider)

            address:tuple = (id_prestador,) + data['address']
            self._insert_address(address)

        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to insert data:", e)

    def _update_provider(self, id:int, provider:tuple):
        self._connect()

        try:
            cur = self.conn.cursor()
            
            statement_old = "SELECT * FROM prestadores WHERE id=?"

            cur.execute(statement_old, (id,))

            provider_old = list(cur.fetchone())
            provider_old.remove(id)
            provider_old = tuple(provider_old)

            provider_new:tuple = ()
            for data_old, data_cur in zip(provider_old, provider):
                data_new = data_old if data_cur is None else data_cur
                provider_new = provider_new + (data_new,)

            statement_new:str = """UPDATE prestadores
            SET nome=?,data_nascimento=?,cpf_cnpj=?,contato=?
            WHERE id=?;"""

            cur.execute(statement_new, provider_new + (id,))

            self.conn.commit()
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to update table:", e)

        finally:
            self.conn.close()

    def _update_address(self, id:int, address:tuple):
        self._connect()

        try:
            cur = self.conn.cursor()
            
            statement_old = "SELECT * FROM enderecos WHERE id_prestador=?"

            cur.execute(statement_old, (id,))

            address_old = list(cur.fetchone())
            address_old.remove(id)
            address_old = tuple(address_old)

            address_new:tuple = ()
            for data_old, data_cur in zip(address_old, address):
                data_new = data_old if data_cur is None else data_cur
                address_new = address_new + (data_new,)
            
            statement_new:str = """UPDATE enderecos
            SET rua=?,numero=?,complemento=?,bairro=?,cidade=?,uf=?,cep=?
            WHERE id_prestador=?;"""

            cur.execute(statement_new, address_new + (id,))

            self.conn.commit()
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to update table:", e)

        finally:
            self.conn.close()

    def verify_id(self, id:int) -> bool:
        self._connect()

        try:

            cur = self.conn.cursor()
            
            statement:str = "SELECT 1 FROM prestadores WHERE id=?;"

            cur.execute(statement, (id,))

            self.conn.commit()

            if cur.fetchone() is None:
                return False
            
            return True
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to verify ID:", e)

        finally:
            self.conn.close()      

    def update(self, id:int, data:dict[str, tuple]):

        try:
            provider:tuple = data['provider']
            address:tuple = data['address']

            if any(x is not None for x in provider):
                self._update_provider(id, provider)
            
            if any(x is not None for x in address):
                self._update_address(id, address)
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to update data:", e)


    def delete(self, id:int):
        self._connect()

        try:
            
            statements:list[str] = [
                "DELETE FROM prestadores WHERE id=?;",
                "DELETE FROM enderecos WHERE id_prestador=?;"
            ]

            for statement in statements:
                self.conn.execute(statement, (id,))

            self.conn.commit()
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to delete data:", e)

        finally:
            self.conn.close()        

    def fetch(self):
        self._connect()

        try:
            cur = self.conn.cursor()

            statement = """SELECT prestadores.id, prestadores.nome, 
            prestadores.data_nascimento, prestadores.cpf_cnpj, 
            prestadores.contato, enderecos.rua, enderecos.numero,
            enderecos.bairro, enderecos.cidade, enderecos.uf,
            enderecos.cep
            FROM prestadores JOIN
            enderecos ON prestadores.id=enderecos.id_prestador;"""

            cur.execute(statement)

            return cur.fetchall()
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to fetch data:", e)

        finally:
            self.conn.close()      


# Example of usage
def main():
    db = Database()

    # Inserting data
    data1 = {
        'provider': ("Beltrano", "DDMMYYYY", "12345678910", "5512999999999"),
        'address': ("Rua", "Número", None, "Bairro", "Cidade", "UF", "99999999")
    }
    data2 = {
        'provider': ("Ciclano", "DDMMYYYY", "12345678910", "5512999999999"),
        'address': ("Rua", "Número", None, "Bairro", "Cidade", "UF", "99999999")
    }
    db.insert(data1)
    db.insert(data2)

    # Fetching data
    rows = db.fetch()
    for row in rows:
        print(row)

    # Deleting provider
    id_del = 1
    print("ID is in the database:", db.verify_id(id_del))
    db.delete(id_del)

    # Updating provider
    id_up = 2
    data_up = {
        'provider': (None, None, None, "5521999999999"),
        'address': (None, None, None, None, None, None, "12345678")
    }
    db.update(id_up, data_up)

    # Fetching data
    rows = db.fetch()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()