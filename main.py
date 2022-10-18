# from endereco import Endereco
# from pessoa import Pessoa



# pessoa = Pessoa('vitor', 20, '88036-050', 'Rua Trajano Margarida')
# pessoa.guardar()
# # print(pessoa.buscar())
# pessoa.idade = 21
# pessoa.atualizar()
# pessoa.endereco.rua = 'Rua João Pedro Haas'
# pessoa.endereco.atualizar()
# # print(pessoa.buscar())

from modules.aparelho.ControladorAparelho import ControladorAparelho
from modules.aparelho.TelaAparelho import TelaAparelho

controlador = ControladorAparelho()
tela = TelaAparelho(controlador)

tela.mostrar_opcoes()
