from abstract.tela import Tela


class TelaAluno(Tela):
  def __init__(self, controlador):
    titulo = 'Alunos'
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome: ', 3, 15]],
      "cpf": ['CPF', str, True, self.inserir_string, ['Insira o CPF: ']],
      "peso": ['CPF', str, True, self.inserir_inteiro, ['Insira o peso: ']],
      "altura": ['CPF', str, True, self.inserir_float, ['Insira a altura: ']],
    }
    opcoes = {
      1: ['Cadastrar um aluno', self.cadastrar],
      2: ['Editar um aluno', self.editar],
      3: ['Listar alunos', self.listar],
      4: ['Deletar um aluno', self.deletar],
    }
    super().__init__(titulo, objeto, opcoes, controlador)