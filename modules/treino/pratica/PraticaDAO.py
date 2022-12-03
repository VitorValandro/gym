from abstract.DAO import DAO
from errors.IsEmptyError import IsEmptyError


class PraticaDAO(DAO):

    def __init__(self) -> None:
        super().__init__('Pratica', 'id')

    def criar(self):
        try:
            with self.connection:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (id INTEGER PRIMARY KEY, repeticoes INTEGER, peso REAL, exercicio INTEGER NOT NULL, treino INTEGER NOT NULL, 
             FOREIGN KEY (exercicio) REFERENCES Exercicio (id),FOREIGN KEY (treino) REFERENCES Treino (id) ON DELETE CASCADE)
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = PraticaDAO.cursor.execute(
                f"SELECT * FROM {PraticaDAO.table_name}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError
