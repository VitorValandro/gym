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
from modules.pessoa.aluno.ControladorAluno import ControladorAluno
from modules.pessoa.aluno.TelaAluno import TelaAluno
from modules.pessoa.professor.ControladorProfessor import ControladorProfessor
from modules.pessoa.professor.TelaProfessor import TelaProfessor
from modules.pratica.ControladorPratica import ControladorPratica
from modules.pratica.TelaPratica import TelaPratica

# controladorAparelho = ControladorAparelho()
# telaAparelho = TelaAparelho(controladorAparelho)

# telaAparelho.mostrar_opcoes()

#controladorExercicio = ControladorExercicio()
#telaExercicio = TelaExercicio(controladorExercicio, controladorAparelho)

#telaExercicio.mostrar_opcoes()

# controladorPratica = ControladorPratica()
# telaPratica = TelaPratica(controladorPratica)

# controladorAluno = ControladorAluno()
# telaAluno = TelaAluno(controladorAluno)

# telaAluno.mostrar_opcoes()

controladorProfessor = ControladorProfessor()
telaProfessor = TelaProfessor(controladorProfessor)

telaProfessor.mostrar_opcoes()