import sys
from abstract.tela import Tela
from modules.aparelho.TelaAparelho import TelaAparelho
from modules.pessoa.aluno.ControladorAluno import ControladorAluno
from modules.pessoa.aluno.TelaAluno import TelaAluno
from modules.exercicio.ControladorExercicio import ControladorExercicio
from modules.pessoa.professor.ControladorProfessor import ControladorProfessor
from modules.pessoa.professor.EntidadeProfessor import Professor
from modules.pessoa.professor.TelaProfessor import TelaProfessor
from modules.exercicio.TelaExercicio import TelaExercicio
from modules.aparelho.ControladorAparelho import ControladorAparelho

controladorAluno = ControladorAluno()
controladorAparelho = ControladorAparelho()
controladorProfessor = ControladorProfessor()
controladorExercicio = ControladorExercicio()

telaAluno = TelaAluno(controladorAluno)
telaAparelho = TelaAparelho(controladorAparelho)
telaProfessor = TelaProfessor(controladorProfessor)
telaExercicio = TelaExercicio(controladorExercicio, telaAparelho)


if __name__ == "__main__":
    # rodando = True
    # tela = TelaPrincipal('CONTROLE DE ACADEMIA', None, None, None)
    # while rodando:
    #   tela.menu_principal()
    telaExercicio.mostrar_opcoes()
