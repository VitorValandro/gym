from datetime import date
import random

from errors.IsEmptyError import IsEmptyError
from errors.NotFound import NotFound
from modules.pessoa.professor.EntidadeProfessor import Professor
from modules.pessoa.professor.turno.EntidadeTurno import Turno

class ControladorProfessor:
  def __init__(self):
    self.__professores = []
    try:
      self.carregar_dados()
    except IsEmptyError:
      pass

  @property
  def colecao(self):
    return self.__professores

  def cadastrar(self, dados: dict, turnos: list):
    try:
      novo_professor = Professor(**dados)
      novo_professor.guardar()
      self.cadastrar_turno(novo_professor.identificador, turnos)
      self.colecao.append(novo_professor)
    except:
      raise ValueError

  def editar(self, id, dados: dict, turnos: list):
    try:
      [objeto, _] = self.buscar_por_id(id)
      for chave, valor in dados.items():
        setattr(objeto, chave, valor)
      objeto.atualizar()
      for turno in turnos:
        turno_editado = Turno(**turno)
        turno_editado.atualizar()
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

  def cadastrar_turno(self, identificador, turnos):
    for turno in turnos:
      turno["professor"] = identificador
      turno["id"] = random.randint(1000, 9999)
      novo_turno = Turno(**turno)
      novo_turno.guardar()

  def deletar_turno(self, id):
    try:
      turno = Turno('', '', 0, 0, id)
      turno.remover()
    except:
      raise ValueError

  def carregar_dados(self):
    # Busca todos os cadastros e popula a listagem
    result = Professor.buscar()
    for dados in result:
      objeto = Professor(**dados)
      turnos = objeto.buscar_turnos()
      objeto.turnos = turnos
      self.colecao.append(objeto)

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
