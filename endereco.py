from entidade import Entidade


class Endereco(Entidade):
  def __init__(self, cep: str, rua: str) -> None:
    super().__init__('Endereco', 'cep')
    self.__cep = cep
    self.__rua = rua

  @property
  def identificador(self):
    return self.__cep
  
  @property
  def rua(self):
    return self.__rua
  
  @rua.setter
  def rua(self, rua):
    self.__rua = rua

  def criar(self):
    try:
      with self.connection:
        self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.tableName} 
            (cep TEXT PRIMARY KEY, rua TEXT)
        """)
      return True
    except Exception:
      return False