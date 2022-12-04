import random
from abstract.DAO import DAO
from errors.IsEmptyError import IsEmptyError


class TurnoDAO(DAO):
    table_name = 'Turno'

    def __init__(self) -> None:
        super().__init__('Turno', 'id')

    def criar(self):
        try:
            with self.connection:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName}
            (
              id INTEGER PRIMARY KEY,
              dia_semana TEXT,
              periodo TEXT,
              carga_horaria INTEGER NOT NULL,
              professor INTEGER NOT NULL,
              FOREIGN KEY (professor) REFERENCES Professor (id) ON DELETE CASCADE)
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = TurnoDAO.cursor.execute(
                f"SELECT * FROM {TurnoDAO.table_name}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError
