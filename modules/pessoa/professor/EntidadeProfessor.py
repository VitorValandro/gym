import random
from errors.IsEmptyError import IsEmptyError
from modules.pessoa.EntidadePessoa import Pessoa


class Professor(Pessoa):
  table_name = 'Professor'
  def __init__(self, nome: str, cpf: str, peso: int, altura: float, salario: float, id = random.randint(1000,9999)) -> None:
    super().__init__(nome, cpf, peso, altura, 'Professor', id)
    self.__salario = salario

  @property
  def salario(self):
    return self.__salario

  @salario.setter
  def salario(self, salario):
    self.__salario = salario

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

  @staticmethod
  def buscar() -> list:
    try:
      res = Professor.cursor.execute(f"SELECT * FROM {Professor.table_name}")
      return [dict(row) for row in res.fetchall()]
    except:
      raise IsEmptyError
