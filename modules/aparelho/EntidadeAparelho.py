import random
from abstract.entidade import Entidade


class Aparelho(Entidade):
  table_name = 'Aparelho'
  def __init__(self, nome: str, quantidade: int, tipo: str, id = random.randint(1000,9999)) -> None:
    super().__init__('Aparelho', 'id')
    self.__id = id
    self.__nome = nome
    self.__quantidade = quantidade
    self.__tipo = tipo

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
  def quantidade(self):
    return self.__quantidade

  @quantidade.setter
  def quantidade(self, quantidade):
    self.__quantidade = quantidade

  @property
  def tipo(self):
    return self.__tipo

  @tipo.setter
  def tipo(self, tipo):
    self.__tipo = tipo

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
    res = Aparelho.cursor.execute(f"SELECT * FROM {Aparelho.table_name}")
    return [dict(row) for row in res.fetchall()]
