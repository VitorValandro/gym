import random
from abstract.entidade import Entidade
from errors.IsEmptyError import IsEmptyError
from modules.pratica.EntidadePratica import Pratica


class Treino(Entidade):
  table_name = 'Treinos'
  def __init__(self, nome: str, pratica: Pratica, id = random.randint(1000,9999)) -> None:
    super().__init__('Treino', 'id')
    self.__id = id
    self.__nome = nome
    self.__pratica = []

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
  def pratica(self):
    return self.__pratica

  @pratica.setter
  def pratica(self, pratica):
    self.__pratica = pratica

  def criar(self):
    try:
      with self.connection:
        self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (id INTEGER PRIMARY KEY, nome TEXT, pratica INTEGER NOT NULL,
             FOREIGN KEY (pratica) REFERENCES Pratica (id))
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
