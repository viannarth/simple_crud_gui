import sqlite3


DATABASE_PATH = './database/database.db'

class Database():
    def __init__(self):
        self.conn = None
        self._create()

    def _connect(self):
        self.conn = sqlite3.connect(DATABASE_PATH)

    def _create(self):
        self._connect()
        cur = self.conn.cursor()
        
        sql_statements:list[str] = [
            """CREATE TABLE IF NOT EXISTS catalogo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    data_nascimento TEXT NOT NULL,
                    cpf TEXT,
                    cnpj TEXT,
                    contato TEXT NOT NULL
                );""",
            """CREATE TABLE IF NOT EXISTS endereco (
                    rua TEXT NOT NULL,
                    numero TEXT NOT NULL, 
                    complemento TEXT,
                    bairro TEXT NOT NULL,
                    cidade TEXT NOT NULL,
                    uf TEXT NOT NULL,
                    cep TEXT NOT NULL
                );"""
        ]

        for statement in sql_statements:
            cur.execute(statement)

        self.conn.commit()
        self.conn.close()


def main():
    db = Database()


if __name__ == "__main__":
    main()