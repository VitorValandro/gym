import random
from errors.IsEmptyError import IsEmptyError
from modules.pessoa.EntidadePessoa import Pessoa


class Aluno(Pessoa):
  table_name = 'Aluno'
  def __init__(self, nome: str, cpf: str, peso: int, altura: float, data_matricula: str, id = None) -> None:
    if not id: id = random.randint(1000,9999)
    super().__init__(nome, cpf, peso, altura, 'Aluno', id)
    self.__data_matricula = data_matricula

  @property
  def data_matricula(self):
    return self.__data_matricula

  @data_matricula.setter
  def data_matricula(self, data_matricula):
    self.__data_matricula = data_matricula

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
      res = Aluno.cursor.execute(f"SELECT * FROM {Aluno.table_name}")
      return [dict(row) for row in res.fetchall()]
    except:
      raise IsEmptyError
