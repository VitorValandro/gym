from abstract.tela import Tela


class TelaExercicio(Tela):
  def __init__(self, controlador, controlador_aparelho):
    titulo = 'Exercícios'
    tipos = {
      1: 'BRAÇOS',
      2: 'PERNAS',
    }
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome', 3, 15]],
      "tipo": ['Tipo', str, True, self.inserir_enum, ['Insira o tipo: ', tipos]],
      "aparelho": ['Aparelho', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do aparelho: ', controlador_aparelho.colecao, 'Aparelhos']],
    }
    opcoes = {
      1: ['Cadastrar um exercicío', self.cadastrar],
      2: ['Editar um exercicío', self.editar],
      3: ['Listar exercícios', self.listar],
      4: ['Deletar um exercicío', self.deletar],
    }
    super().__init__(titulo, objeto, opcoes, controlador)