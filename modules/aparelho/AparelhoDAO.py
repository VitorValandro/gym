from abstract.DAO import DAO
from errors.IsEmptyError import IsEmptyError


class AparelhoDAO(DAO):
    table_name = 'Aparelho'

    def __init__(self) -> None:
        super().__init__('Aparelho', 'id')

    def criar(self):
        try:
            with self.connection:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (id INTEGER PRIMARY KEY, nome TEXT, quantidade INTEGER, tipo TEXT)
        """)
            return True
        except Exception:
            return False

    @staticmethod
    def buscar() -> list:
        try:
            res = AparelhoDAO.cursor.execute(
                f"SELECT * FROM {AparelhoDAO.table_name}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError
