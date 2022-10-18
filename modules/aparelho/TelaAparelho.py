from abstract.tela import Tela


class TelaAparelho(Tela):
  def __init__(self, controlador):
    titulo = 'PESSOAS'
    tipos = {
      1: 'CROSS',
      2: 'SUPINO',
      3: 'HACK'
    }
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome', 3, 15]],
      "quantidade": ['Quantidade', int, True, self.inserir_inteiro, ['Insira a quantidade: ',]],
      "tipo": ['Tipo', str, True, self.inserir_enum, ['Insira o tipo: ', tipos]]
    }
    opcoes = {
      1: ['Cadastrar um item', self.cadastrar],
      2: ['Editar um item', self.cadastrar],
      3: ['Listar itens', self.cadastrar],
      4: ['Deletar um item', self.cadastrar],
    }
    super().__init__(titulo, objeto, opcoes)
    self.__controlador = controlador

  def cadastrar(self):
    dados = self.pegar_dados()
    self.__controlador.cadastrar(dados)