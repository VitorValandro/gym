import random
from abstract.entidade import Entidade
from errors.IsEmptyError import IsEmptyError
from modules.exercicio.EntidadeExercicio import Exercicio
from modules.treino.EntidadeTreino import Treino


class Pratica(Entidade):
  table_name = 'Pratica'
  def __init__(self, repeticoes: int, peso: float, exercicio: Exercicio,treino: Treino, id = None) -> None:
    if not id: id = random.randint(1000,9999)
    super().__init__('Pratica', 'id')
    self.__id = id
    self.__repeticoes = repeticoes
    self.__peso = peso
    self.__exercicio = exercicio
    self.__treino = treino

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
            (id INTEGER PRIMARY KEY, repeticoes INTEGER, peso REAL, exercicio INTEGER NOT NULL, treino INTEGER NOT NULL, 
             FOREIGN KEY (exercicio) REFERENCES Exercicio (id),FOREIGN KEY (treino) REFERENCES Treino (id) ON DELETE CASCADE)
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
