import random
from abstract.entidade import Entidade
from errors.IsEmptyError import IsEmptyError
from modules.pessoa.aluno.EntidadeAluno import Aluno
from modules.pessoa.professor.EntidadeProfessor import Professor
from modules.treino.EntidadeTreino import Treino

class Historico(Entidade):
  table_name = 'Historico'
  def __init__(
      self,
      data: str,
      tempo: int,
      avaliacao: str,
      aluno: Aluno,
      professor: Professor,
      treino: Treino,
      id = None
    ) -> None:
    super().__init__('Historico', 'id')
    if not id: id = random.randint(1000,9999)
    self.__id = id
    self.__data = data
    self.__tempo = tempo
    self.__avaliacao = avaliacao
    self.__aluno = aluno
    self.__professor = professor
    self.__treino = treino

  @property
  def identificador(self):
    return self.__id

  @property
  def data(self):
    return self.__data
  
  @data.setter
  def data(self, data):
    self.__data = data

  @property
  def tempo(self):
    return self.__tempo
  
  @tempo.setter
  def tempo(self, tempo):
    self.__tempo = tempo

  @property
  def avaliacao(self):
    return self.__avaliacao
  
  @avaliacao.setter
  def avaliacao(self, avaliacao):
    self.__avaliacao = avaliacao
  
  @property
  def aluno(self):
    return self.__aluno
  
  @aluno.setter
  def aluno(self, aluno):
    self.__aluno = aluno
  
  @property
  def professor(self):
    return self.__professor
  
  @professor.setter
  def professor(self, professor):
    self.__professor = professor

  @property
  def treino(self):
    return self.__treino
  
  @treino.setter
  def treino(self, treino):
    self.__treino = treino

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
      res = Historico.cursor.execute(f'''
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
