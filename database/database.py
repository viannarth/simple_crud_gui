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
                        cpf TEXT,
                        cnpj TEXT,
                        contato TEXT NOT NULL
                    );""",
                """CREATE TABLE IF NOT EXISTS enderecos (
                        id INTERGER PRIMARY KEY,
                        id_prestador INT NOT NULL,
                        rua TEXT NOT NULL,
                        numero TEXT NOT NULL, 
                        complemento TEXT,
                        bairro TEXT NOT NULL,
                        cidade TEXT NOT NULL,
                        uf TEXT NOT NULL,
                        cep TEXT NOT NULL,
                        FOREIGN KEY (id_prestador) REFERENCES prestadores (id) ON DELETE CASCADE
                    );"""
            ]

            for statement in sql_statements:
                self.conn.execute(statement)

            self.conn.commit()
            
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print("Failed to create tables:", e)

        finally:
            self.conn.close()
            

def main():
    db = Database()


if __name__ == "__main__":
    main()