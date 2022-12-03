import random
from errors.IsEmptyError import IsEmptyError
from abstract.DAO import DAO
from modules.pessoa.professor.turno.TurnoDAO import TurnoDAO


class ProfessorDAO(DAO):
    table_name = 'Professor'

    def __init__(self) -> None:
        super().__init__('Professor', 'id')

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
              salario TEXT
            )
        """)
            return True
        except Exception:
            raise

    def buscar_turnos(self) -> list:
        try:
            res = ProfessorDAO.cursor.execute(
                f"SELECT * FROM {TurnoDAO.table_name} WHERE professor = {self.identificador}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError

    @staticmethod
    def buscar() -> list:
        try:
            res = ProfessorDAO.cursor.execute(
                f"SELECT * FROM {ProfessorDAO.table_name}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError
