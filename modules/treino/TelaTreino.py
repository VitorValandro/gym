from abstract.tela import Tela


class TelaTreino(Tela):
  def __init__(self, controlador, controlador_exercicio):
    titulo = 'Pratica'
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome']],
      "peso": ['Peso', str, True, self.inserir_float, ['Insira o peso: ', 0, 100]],
      "exercicio": ['Exercicio', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do exercicio: ', controlador_exercicio.colecao, 'Exercicios']],
    }
    opcoes = {
      1: ['Cadastrar um treino', self.cadastrar],
      2: ['Editar um treino', self.editar],
      3: ['Listar treinos', self.listar],
      4: ['Deletar um treino', self.deletar],
    }
    super().__init__(titulo, objeto, opcoes, controlador)