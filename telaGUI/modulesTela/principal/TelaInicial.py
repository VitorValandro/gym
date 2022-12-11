import PySimpleGUI as sg
from telaGUI.modulesTela.aparelho.TelaInicial import TelaInicial as Taparelho
from telaGUI.modulesTela.aluno.TelaInicial import TelaInicial as Taluno
from telaGUI.modulesTela.professor import TelaInicial as Tprof
from telaGUI.modulesTela.exercicio.TelaInicial import TelaInicial as Texe
from telaGUI.modulesTela.treino.TelaInicial import TelaInicial as Ttreino
from telaGUI.modulesTela.historico import TelaInicial as Thist
from telaGUI.modulesTela.relatorios.TelaInicial import TelaInicial as Trelatorio



class TelaInicial:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('-- CONTROLE DE ACADEMIA --')],
            [sg.Text('1: Tela de Alunos')],
            [sg.Text('2: Tela de Professores')],
            [sg.Text('3: Tela de Aparelhos')],
            [sg.Text('4: Tela de Exercícios')],
            [sg.Text('5: Tela de Treinos')],
            [sg.Text('6: Tela de Históricos')],
            [sg.Text('7: Tela de Relatórios')],
            [sg.Text('8: Sair')],
            [sg.Button('Escolha uma das telas'), sg.Input(size=3, key="escolha")]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()
    
    def iniciar(self):
        escolha = self.values['escolha']
        if(escolha == '1'):
            tela = Taluno()
            tela.iniciar()
        elif(escolha == '2'):
            tela2 = Tprof()
            tela2.iniciar()
        elif(escolha == '3'):
            tela3 = Taparelho()
            tela3.iniciar()
        elif(escolha == '4'):
            tela4 = Texe()
            tela4.iniciar()
        elif(escolha == '5'):
            tela5 = Ttreino()
            tela5.iniciar()
        elif(escolha == '6'):
            tela6 = Thist()
            tela6.iniciar()
        elif(escolha == '7'):
            tela7 = Trelatorio()
            tela7.iniciar()
        elif(escolha == '8'):
            return False
        else:
            sg.Popup('Digite um número válido', keep_on_top=True)
        return True

