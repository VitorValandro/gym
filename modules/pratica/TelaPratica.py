from abstract.tela import Tela
from modules.treino.ControladorTreino import ControladorTreino


class TelaPratica(Tela):
  def __init__(self, controlador, controlador_exercicio, controlador_treino):
    titulo = 'Pratica'
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "repeticoes": ['Repeticoes', int, True, self.inserir_inteiro, ['Insira o numero de repeticoes: ']],
      "peso": ['Peso', float, True, self.inserir_float, ['Insira o peso: ']],
      "exercicio": ['Exercicio', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do exercicio: ', controlador_exercicio.colecao, 'Exercicios']],
      "treino": ['Treino', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do treino: ', controlador_treino.colecao, 'Treinos']],
    }
    opcoes = {
      1: ['Cadastrar uma pratica ao treino', self.cadastrar],
      2: ['Editar uma pratica', self.editar],
      3: ['Listar praticas', self.listar],
      4: ['Deletar uma pratica', self.deletar],
    }
    super().__init__(titulo, objeto, opcoes, controlador)
