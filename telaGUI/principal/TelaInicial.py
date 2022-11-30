import PySimpleGUI as sg

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
        print(self.values)

tela = TelaInicial()
tela.iniciar()