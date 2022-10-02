from entidade import Entidade


class Pessoa(Entidade):
  def __init__(self, name, idade) -> None:
    super().__init__('Pessoa', 'name')
    self.__name = name
    self.__idade = idade

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

  def criar(self):
    try:
      with self.connection:
        self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (name TEXT, idade INTEGER)
        """)
      return True
    except Exception:
      return False
