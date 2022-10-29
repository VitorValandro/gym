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
from modules.exercicio.ControladorExercicio import ControladorExercicio
from modules.exercicio.TelaExercicio import TelaExercicio
from modules.pratica.ControladorPratica import ControladorPratica
from modules.pratica.TelaPratica import TelaPratica
from modules.pessoa.aluno.ControladorAluno import ControladorAluno
from modules.treino.ControladorTreino import ControladorTreino
from modules.treino.TelaTreino import TelaTreino

controladorAparelho = ControladorAparelho()
telaAparelho = TelaAparelho(controladorAparelho)

# telaAparelho.mostrar_opcoes()

controladorExercicio = ControladorExercicio()
telaExercicio = TelaExercicio(controladorExercicio, controladorAparelho)

telaExercicio.mostrar_opcoes()

controladorPratica = ControladorPratica()
telaPratica = TelaPratica(controladorPratica, controladorExercicio)
# telaPratica.mostrar_opcoes()

controladorAluno = ControladorAluno()

# controladorTreino = ControladorTreino()
# telaTreino = TelaTreino(controladorTreino, controladorAluno)
# telaTreino.mostrar_opcoes()




