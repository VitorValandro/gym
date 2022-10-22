import random
from abstract.entidade import Entidade
from errors.IsEmptyError import IsEmptyError
from exercicio import EntidadeExercicio


class Pratica(Entidade):
  table_name = 'Pratica'
  def __init__(self, repeticoes: int, peso: float, exercicio: EntidadeExercicio, id = random.randint(1000,9999)) -> None:
    super().__init__('Pratica', 'id')
    self.__id = id
    self.__repeticoes = repeticoes
    self.__peso = peso
    self.__exercicio = []

  @property
  def identificador(self):
    return self.__id

  @property
  def repeticoes(self):
    return self.__repeticoes

  @repeticoes.setter
  def repeticoes(self, repeticoes):
    self.__repeticoes = repeticoes

  @property
  def peso(self):
    return self.__peso

  @peso.setter
  def peso(self, peso):
    self.__peso = peso
   
  @property
  def exercicio(self):
    return self.__exercicio

  @exercicio.setter
  def exercicio(self, exercicio):
    self.__exercicio = exercicio

  def criar(self):
    try:
      with self.connection:
        self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (id INTEGER PRIMARY KEY, repeticoes INTEGER, peso FLOAT, exercicio INTEGER NOT NULL,
             FOREIGN KEY (exercicio) REFERENCES Exercicio (id))
        """)
      return True
    except Exception:
      raise

  @staticmethod
  def buscar() -> list:
    try:
      res = Pratica.cursor.execute(f"SELECT * FROM {Pratica.table_name}")
      return [dict(row) for row in res.fetchall()]
    except:
      raise IsEmptyError
