from abstract.DAO import DAO
from errors.IsEmptyError import IsEmptyError


class TreinoDAO(DAO):
    table_name = 'Treino'

    def __init__(self) -> None:
        super().__init__('Treino', 'id')

    def criar(self):
        try:
            with self.connection:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (id INTEGER PRIMARY KEY, nome TEXT, aluno INTEGER NOT NULL,
             FOREIGN KEY (aluno) REFERENCES Aluno (id))
        """)
            return True
        except Exception:
            raise

    def buscar_praticas(self) -> list:
        try:
            res = TreinoDAO.cursor.execute(f'''
        SELECT 
          Pratica.id,
          Pratica.repeticoes,
          Pratica.peso,
          Pratica.treino,
          Exercicio.nome as exercicio
        FROM
          Pratica
          INNER JOIN Exercicio ON Exercicio.id = Pratica.exercicio
        WHERE 
          treino = {self.identificador};
      ''')
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError

    @staticmethod
    def buscar() -> list:
        try:
            res = TreinoDAO.cursor.execute(
                f"SELECT * FROM {TreinoDAO.table_name}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError
