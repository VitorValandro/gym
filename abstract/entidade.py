from abc import ABC, abstractmethod
import sqlite3


class Entidade(ABC):
  connection = sqlite3.connect('test.db')
  connection.row_factory = sqlite3.Row   
  cursor = connection.cursor()

  @abstractmethod
  def __init__(self, name: str, coluna_id: str) -> None:
    self.coluna_id = coluna_id
    self.tableName = name
    self.connection = Entidade.connection
    self.cursor = Entidade.cursor
    self.criar()

  @property
  def atributos(self) -> dict:
    return {
      k.replace(f'_{self.tableName}__', ''): v
      for k, v in self.__dict__.items() if k.startswith(f'_{self.tableName}')
    }

  @property
  @abstractmethod
  def identificador(self):
    ''' GETTER: Deve retornar o valor da propriedade identificadora da instancia '''

  @abstractmethod
  def criar(self):
    ''' Deve criar a cláusula para criar a tabela '''

  @staticmethod
  @abstractmethod
  def buscar():
    ''' DEVE FAZER UM SELECT ALL NA TABELA DA ENTIDADE '''
  
  def guardar(self):
    valores = tuple([v.identificador if isinstance(v, Entidade) else v for v in self.atributos.values()])
    parametros = '('+','.join('?' for _ in valores)+')'

    try:
      with self.connection:
        self.cursor.execute(f"""
          INSERT OR IGNORE INTO {self.tableName} 
          VALUES {parametros}
        """, valores)
        return True
    except Exception:
      raise

  def atualizar(self):
    set_statement = ', '.join([f"{k} = '{v}'" for k, v in self.atributos.items() if not isinstance(v, Entidade) and v is not None])

    try:
      with self.connection:
        self.cursor.execute(f"""
          UPDATE {self.tableName} 
          SET {set_statement}
          WHERE {self.coluna_id} = '{self.identificador}'
        """)
        return True
    except Exception:
      raise

  def remover(self):
    try:
      with self.connection:
        self.cursor.execute(f"""
          DELETE 
          FROM {self.tableName}
          WHERE {self.coluna_id} = '{self.identificador}'
        """)
        return True
    except Exception:
      raise

  def __eq__(self, other):
    if self.identificador == other.identificador: 
      return True
    else:
      return False
