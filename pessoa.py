from endereco import Endereco
from abstract.entidade import Entidade


class Pessoa(Entidade):
  def __init__(self, name, idade, cep: str, rua: str) -> None:
    super().__init__('Pessoa', 'name')
    self.__name = name
    self.__idade = idade
    self.__endereco = Endereco(cep, rua)
    self.__endereco.guardar()

  @property
  def identificador(self):
    return self.__name
  
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, name):
    self.__name = name
  
  @property
  def idade(self):
    return self.__idade
  
  @idade.setter
  def idade(self, idade):
    self.__idade = idade

  @property
  def endereco(self):
    return self.__endereco

  def criar(self):
    try:
      with self.connection:
        self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (name TEXT PRIMARY KEY, idade INTEGER, endereco_cep TEXT, 
            FOREIGN KEY (endereco_cep) REFERENCES Endereco (cep))
        """)
      return True
    except Exception:
      return False
