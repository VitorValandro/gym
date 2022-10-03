from endereco import Endereco
from pessoa import Pessoa

pessoa = Pessoa('vitor', 20, '88036-050', 'Rua Trajano Margarida')
pessoa.guardar()
# print(pessoa.buscar())
pessoa.idade = 21
pessoa.atualizar()
pessoa.endereco.rua = 'Rua João Pedro Haas'
pessoa.endereco.atualizar()
# print(pessoa.buscar())
