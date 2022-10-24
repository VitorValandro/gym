import random
from abstract.entidade import Entidade
from errors.IsEmptyError import IsEmptyError


class Exercicio(Entidade):
  table_name = 'Exercicio'
  def __init__(self, nome: str, tipo: str, aparelho: int, id = random.randint(1000,9999)) -> None:
    super().__init__('Exercicio', 'id')
    self.__id = id
    self.__nome = nome
    self.__tipo = tipo
    self.__aparelho = aparelho

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
  def tipo(self):
    return self.__tipo

  @tipo.setter
  def tipo(self, tipo):
    self.__tipo = tipo
  
  @property
  def aparelho(self):
    return self.__aparelho

  @aparelho.setter
  def aparelho(self, aparelho):
    self.__aparelho = aparelho

  def criar(self):
    try:
      with self.connection:
        self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (id INTEGER PRIMARY KEY, nome TEXT, tipo TEXT, aparelho INTEGER NOT NULL,
             FOREIGN KEY (aparelho) REFERENCES Aparelho (id) ON DELETE RESTRICT)
        """)
      return True
    except Exception:
      raise

  @staticmethod
  def buscar() -> list:
    try:
      res = Exercicio.cursor.execute(f"SELECT * FROM {Exercicio.table_name}")
      return [dict(row) for row in res.fetchall()]
    except:
      raise IsEmptyError
