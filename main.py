from modules.aparelho.TelaAparelho import TelaAparelho
from modules.historico.ControladorHistorico import ControladorHistorico
from modules.historico.TelaHistorico import TelaHistorico
from modules.pessoa.aluno.ControladorAluno import ControladorAluno
from modules.pessoa.aluno.TelaAluno import TelaAluno
from modules.pessoa.professor.ControladorProfessor import ControladorProfessor
from modules.treino.ControladorTreino import ControladorTreino
from modules.aparelho.ControladorAparelho import ControladorAparelho

from modules.treino.TelaTreino import TelaTreino
from modules.exercicio.TelaExercicio import TelaExercicio
from modules.exercicio.ControladorExercicio import ControladorExercicio

controladorAluno = ControladorAluno()
controladorExercicio = ControladorExercicio()
controladorAparelho = ControladorAparelho()
controladorTreino = ControladorTreino()
controladorProfessor = ControladorProfessor()
controladorHistorico = ControladorHistorico()

# telaAluno = TelaAluno(controladorAluno)
# telaAluno.mostrar_opcoes()

# telaAparelho = TelaAparelho(controladorAparelho)
# telaAparelho.mostrar_opcoes()

# telaExercicio = TelaExercicio(controladorExercicio, controladorAparelho)
# telaExercicio.mostrar_opcoes()

# telaTreino = TelaTreino(controladorTreino, controladorAluno, controladorExercicio)
# telaTreino.mostrar_opcoes()

telaHistorico = TelaHistorico(controladorHistorico, controladorAluno, controladorProfessor, controladorTreino)
telaHistorico.mostrar_opcoes()