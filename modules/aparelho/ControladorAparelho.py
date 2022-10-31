from errors.IsEmptyError import IsEmptyError
from errors.NotFound import NotFound
from modules.aparelho.EntidadeAparelho import Aparelho

class ControladorAparelho:
  def __init__(self):
    self.__aparelhos = []
    try:
      self.carregar_dados()
    except IsEmptyError:
      pass

  @property
  def colecao(self):
    return self.__aparelhos

  @colecao.setter
  def colecao(self, colecao):
    self.__aparelhos = colecao

  def cadastrar(self, dados: dict):
    try:
      novo_aparelho = Aparelho(**dados)
      novo_aparelho.guardar()
      self.carregar_dados()
    except:
      raise ValueError

  def editar(self, id, dados: dict):
    try:
      [aparelho, _] = self.buscar_por_id(id)
      for chave, valor in dados.items():
        setattr(aparelho, chave, valor)
      aparelho.atualizar()
    except (IsEmptyError, NotFound):
      raise
    except:
      raise ValueError

  def deletar(self, id):
    try:
      [aparelho, _] = self.buscar_por_id(id)
      aparelho.remover()
      self.carregar_dados()
    except NotFound:
      raise NotFound
    except:
      raise ValueError

  def carregar_dados(self):
    # Busca todos os cadastros e popula a listagem
    result = Aparelho.buscar()
    self.colecao = []
    for dados in result:
      aparelho = Aparelho(**dados)
      self.colecao.append(aparelho)

  def buscar_por_id(self, id):
    # Recebe um id, busca ele na lista e devolve o objeto e o indice
    if not len(self.colecao):
      raise IsEmptyError
    try:
      index = [x.identificador for x in self.colecao].index(id)
    except ValueError:
      raise NotFound
    objeto = self.colecao[index]
    return (objeto, index)
