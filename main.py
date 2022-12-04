import sys
from abstract.tela import Tela
from modules.aparelho.TelaAparelho import TelaAparelho
from modules.historico.ControladorHistorico import ControladorHistorico
from modules.historico.TelaHistorico import TelaHistorico
from modules.pessoa.aluno.ControladorAluno import ControladorAluno
from modules.pessoa.aluno.TelaAluno import TelaAluno
from modules.pessoa.professor.ControladorProfessor import ControladorProfessor
from modules.pessoa.professor.TelaProfessor import TelaProfessor
from modules.relatorios.ControladorRelatorios import ControladorRelatorios
from modules.relatorios.TelaRelatorios import TelaRelatorios
from modules.treino.ControladorTreino import ControladorTreino
from modules.aparelho.ControladorAparelho import ControladorAparelho

from modules.treino.TelaTreino import TelaTreino
from modules.exercicio.TelaExercicio import TelaExercicio
from modules.exercicio.ControladorExercicio import ControladorExercicio

controladorAluno = ControladorAluno()
controladorAparelho = ControladorAparelho()
controladorExercicio = ControladorExercicio()
controladorProfessor = ControladorProfessor()
controladorTreino = ControladorTreino()
controladorHistorico = ControladorHistorico()
controladorRelatorios = ControladorRelatorios()

telaAluno = TelaAluno(controladorAluno)
telaAparelho = TelaAparelho(controladorAparelho)
telaExercicio = TelaExercicio(controladorExercicio, telaAparelho)
telaProfessor = TelaProfessor(controladorProfessor)
telaTreino = TelaTreino(controladorTreino, telaAluno, telaExercicio)
telaHistorico = TelaHistorico(
    controladorHistorico, telaAluno, telaProfessor, telaTreino)
telaRelatorios = TelaRelatorios(
    controladorRelatorios, telaAluno, telaProfessor)


class TelaPrincipal(Tela):
    def __init__(self, titulo, objeto, opcoes, controlador):
        super().__init__(titulo, objeto, opcoes, controlador)

    def menu_principal(self):
        telas = {
            1: ['Tela de Alunos', telaAluno.mostrar_opcoes],
            2: ['Tela de Professores', telaProfessor.mostrar_opcoes],
            3: ['Tela de Aparelhos', telaAparelho.mostrar_opcoes],
            4: ['Tela de Exercícios', telaExercicio.mostrar_opcoes],
            5: ['Tela de Treinos', telaTreino.mostrar_opcoes],
            6: ['Tela de Históricos', telaHistorico.mostrar_opcoes],
            7: ['Tela de Relatórios', telaRelatorios.mostrar_opcoes],
            8: ['Sair', sys.exit]
        }
        print('\n-- CONTROLE DE ACADEMIA --\n')
        for opcao, tela in telas.items():
            print(f"{opcao} - {tela[0]}")
        opcao_escolhida = self.inserir_inteiro(
            'Escolha uma tela: ', list(telas.keys()))
        telas[opcao_escolhida][1]()


if __name__ == "__main__":
    rodando = True
    tela = TelaPrincipal('CONTROLE DE ACADEMIA', None, None, None)
    while rodando:
        tela.menu_principal()
