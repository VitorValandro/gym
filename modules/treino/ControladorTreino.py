from errors.IsEmptyError import IsEmptyError
from errors.NotFound import NotFound
from EntidadePratica import Pratica

class ControladorPratica:
  def __init__(self):
    self.__pratica = []
    try:
      self.carregar_dados()
    except IsEmptyError:
      pass

  @property
  def colecao(self):
    return self.__pratica

  def cadastrar(self, dados: dict):
    try:
      nova_pratica = Pratica(**dados)
      nova_pratica.guardar()
      self.colecao.append(nova_pratica)
    except:
      raise ValueError

  def editar(self, id, dados: dict):
    try:
      [objeto, _] = self.buscar_por_id(id)
      for chave, valor in dados.items():
        setattr(objeto, chave, valor)
      objeto.atualizar()
    except (IsEmptyError, NotFound):
      raise
    except:
      raise ValueError

  def deletar(self, id):
    try:
      [objeto, _] = self.buscar_por_id(id)
      objeto.remover()
    except NotFound:
      raise NotFound
    except:
      raise ValueError

  def carregar_dados(self):
    # Busca todos os cadastros e popula a listagem
    result = Pratica.buscar()
    for dados in result:
      pratica = Pratica(**dados)
      self.colecao.append(pratica)

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
