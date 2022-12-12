import PySimpleGUI as sg

class TelaDelete:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Digite o ID que você deseja deletar'), sg.Input(size=3)],
            [sg.Button('Deletar')]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()
    
    def iniciar(self):
        print(self)
