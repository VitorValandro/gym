
from datetime import datetime

from errors.IsEmptyError import IsEmptyError
from errors.NotFound import NotFound
from modules.historico.EntidadeHistorico import Historico

class ControladorHistorico:
  def __init__(self):
    self.__historicos = []
    try:
      self.carregar_dados()
    except IsEmptyError:
      pass

  @property
  def colecao(self):
    return self.__historicos

  def cadastrar(self, dados: dict):
    try:
      dados["data"] = datetime.now()
      novo_historico = Historico(**dados)
      novo_historico.data = datetime.now()
      novo_historico.guardar()
      self.colecao.append(novo_historico)
    except:
      raise ValueError

  def carregar_dados(self):
    # Busca todos os cadastros e popula a listagem
    result = Historico.buscar()
    for dados in result:
      historico = Historico(**dados)
      self.colecao.append(historico)

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
