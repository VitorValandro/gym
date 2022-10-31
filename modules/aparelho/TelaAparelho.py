from abstract.tela import Tela
from errors.NotFound import NotFound


class TelaAparelho(Tela):
  def __init__(self, controlador):
    titulo = 'Aparelhos'
    tipos = {
      1: 'FIXOS',
      2: 'EXTENSORAS/FLEXORAS',
      3: 'LIVRES',
      4: 'HALTERES',
      5: 'CARDIOVASCULARES',
      6: 'CROSS'
    }
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome', 3, 15]],
      "quantidade": ['Quantidade', int, True, self.inserir_inteiro, ['Insira a quantidade: ',]],
      "tipo": ['Tipo', str, True, self.inserir_enum, ['Insira o tipo: ', tipos]]
    }
    opcoes = {
      1: ['Cadastrar um item', self.cadastrar],
      2: ['Editar um item', self.editar],
      3: ['Listar itens', self.listar],
      4: ['Deletar um item', self.deletar],
    }
    super().__init__(titulo, objeto, opcoes, controlador)