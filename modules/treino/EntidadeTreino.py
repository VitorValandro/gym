import random
from abstract.entidade import Entidade
from errors.IsEmptyError import IsEmptyError
from modules.pessoa.aluno.EntidadeAluno import Aluno


class Treino(Entidade):
  table_name = 'Treino'
  def __init__(self, nome: str, aluno: Aluno, id = random.randint(1000,9999)) -> None:
    super().__init__('Treino', 'id')
    self.__id = id
    self.__nome = nome
    self.__aluno = aluno


  @property
  def identificador(self):
    return self.__id

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome
   
  @property
  def aluno(self):
    return self.__aluno

  @aluno.setter
  def aluno(self, aluno):
    self.__aluno = aluno

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

  @staticmethod
  def buscar() -> list:
    try:
      res = Treino.cursor.execute(f"SELECT * FROM {Treino.table_name}")
      return [dict(row) for row in res.fetchall()]
    except:
      raise IsEmptyError
