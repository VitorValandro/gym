import random
from errors.IsEmptyError import IsEmptyError
from abstract.DAO import DAO


class AlunoDAO(DAO):
    table_name = 'Aluno'

    def __init__(self) -> None:
        super().__init__('Aluno', 'id')

    def criar(self):
        try:
            with self.connection:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (
              id INTEGER PRIMARY KEY, 
              nome TEXT, 
              cpf TEXT, 
              peso INTEGER,
              altura REAL,
              data_matricula TEXT
            )
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = AlunoDAO.cursor.execute(
                f"SELECT * FROM {AlunoDAO.table_name}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError
