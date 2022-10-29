from errors.IsEmptyError import IsEmptyError
from errors.NotFound import NotFound
from modules.pessoa.aluno.EntidadeAluno import Aluno
from modules.treino.EntidadeTreino import Treino

class ControladorTreino:
  def __init__(self):
    self.__treino = []
    try:
      print("teste 1")
      self.carregar_dados()
    except IsEmptyError:
      pass

  @property
  def colecao(self):
    return self.__treino

  def cadastrar(self, dados: dict):
    try:
      novo_treino = Treino(**dados)
      novo_treino.guardar()
      self.colecao.append(novo_treino)
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
    result = Treino.buscar()
    for dados in result:
      treino = Treino(**dados)
      self.colecao.append(treino)
    

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
