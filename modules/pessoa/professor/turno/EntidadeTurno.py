import random
from abstract.entidade import Entidade
from errors.IsEmptyError import IsEmptyError


# FAZER COMPOSIÇÃO
class Turno(Entidade):
  table_name = 'Turno'
  def __init__(self, dia_semana: str, periodo: str, carga_horaria: int, professor: int, id = random.randint(1000,9999)) -> None:
    super().__init__('Turno', 'id')
    self.__id = id
    self.__dia_semana = dia_semana
    self.__periodo = periodo
    self.__carga_horaria = carga_horaria
    self.__professor = professor

  @property
  def identificador(self):
    return self.__id

  @property
  def dia_semana(self):
    return self.__dia_semana

  @dia_semana.setter
  def dia_semana(self, dia_semana):
    self.__dia_semana = dia_semana

  @property
  def periodo(self):
    return self.__periodo

  @periodo.setter
  def periodo(self, periodo):
    self.__periodo = periodo
  
  @property
  def carga_horaria(self):
    return self.__carga_horaria

  @carga_horaria.setter
  def carga_horaria(self, carga_horaria):
    self.__carga_horaria = carga_horaria
  
  @property
  def professor(self):
    return self.__professor

  @professor.setter
  def professor(self, professor):
    self.__professor = professor

  def criar(self):
    try:
      with self.connection:
        self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName}
            (
              id INTEGER PRIMARY KEY,
              dia_semana TEXT,
              periodo TEXT,
              carga_horaria INTEGER NOT NULL,
              FOREIGN KEY (professor) REFERENCES Professor (id) ON DELETE RESTRICT)
        """)
      return True
    except Exception:
      raise

  @staticmethod
  def buscar() -> list:
    try:
      res = Turno.cursor.execute(f"SELECT * FROM {Turno.table_name}")
      return [dict(row) for row in res.fetchall()]
    except:
      raise IsEmptyError