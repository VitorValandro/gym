from abstract.tela import Tela


class TelaProfessor(Tela):
  def __init__(self, controlador):
    titulo = 'Professores'
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome: ', 3, 15]],
      "cpf": ['CPF', str, True, self.inserir_string, ['Insira o CPF: ']],
      "peso": ['Peso', str, True, self.inserir_inteiro, ['Insira o peso: ']],
      "altura": ['Altura', str, True, self.inserir_float, ['Insira a altura: ']],
      "salario": ['Salário', str, True, self.inserir_float, ['Insira o salário: ']],
    }
    opcoes = {
      1: ['Cadastrar um professor', self.cadastrar],
      2: ['Editar um professor', self.editar],
      3: ['Listar professores', self.listar],
      4: ['Deletar um professor', self.deletar],
    }
    super().__init__(titulo, objeto, opcoes, controlador)