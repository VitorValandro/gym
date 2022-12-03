import random
from abstract.DAO import DAO
from errors.IsEmptyError import IsEmptyError


class ExercicioDAO(DAO):
    table_name = 'Exercicio'

    def __init__(self) -> None:
        super().__init__('Exercicio', 'id')

    def criar(self):
        try:
            with self.connection:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (id INTEGER PRIMARY KEY, nome TEXT, tipo TEXT, aparelho INTEGER NOT NULL,
             FOREIGN KEY (aparelho) REFERENCES Aparelho (id) ON DELETE RESTRICT)
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = ExercicioDAO.cursor.execute(
                f"SELECT * FROM {ExercicioDAO.table_name}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError
