from errors.IsEmptyError import IsEmptyError
from abstract.DAO import DAO


class HistoricoDAO(DAO):
    table_name = 'Historico'

    def __init__(self):
        super().__init__('Historico', 'id')

    def criar(self):
        try:
            with self.connection:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (
              id INTEGER PRIMARY KEY, 
              data TEXT,
              tempo TEXT,
              avaliacao TEXT,
              aluno INTEGER NOT NULL,
              professor INTEGER NOT NULL,
              treino INTEGER NOT NULL,
              
              FOREIGN KEY (aluno) REFERENCES Aluno (id),
              FOREIGN KEY (professor) REFERENCES Professor (id),
              FOREIGN KEY (treino) REFERENCES Treino (id)
            )
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = HistoricoDAO.cursor.execute(f'''
        SELECT 
          Historico.avaliacao,
          Historico.data,
          Historico.tempo,
          Aluno.nome as aluno,
          Professor.nome as professor,
          Treino.nome as treino
        FROM 
          Historico
          INNER JOIN Aluno ON Aluno.id = Historico.aluno
          INNER JOIN Professor ON Professor.id = Historico.professor
          INNER JOIN Treino ON Treino.id = Historico.treino
      ''')
            return [dict(row) for row in res.fetchall()]
        except:
            raise IsEmptyError
