from errors.IsEmptyError import IsEmptyError
from errors.NotFound import NotFound
from modules.exercicio.EntidadeExercicio import Exercicio

class ControladorExercicio:
  def __init__(self):
    self.__exercicios = []
    try:
      self.carregar_dados()
    except IsEmptyError:
      pass

  @property
  def colecao(self):
    return self.__exercicios

  @colecao.setter
  def colecao(self, colecao):
    self.__exercicios = colecao

  def cadastrar(self, dados: dict):
    try:
      novo_exercicio = Exercicio(**dados)
      novo_exercicio.guardar()
      self.carregar_dados()
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
      self.carregar_dados()
    except NotFound:
      raise NotFound
    except:
      raise ValueError

  def carregar_dados(self):
    # Busca todos os cadastros e popula a listagem
    result = Exercicio.buscar()
    self.colecao = []
    for dados in result:
      exercicio = Exercicio(**dados)
      self.colecao.append(exercicio)

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
