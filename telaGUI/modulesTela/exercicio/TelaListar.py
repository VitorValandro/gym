import PySimpleGUI as sg

class TelaListar:
    def __init__(self):
        nomes = "teste"
        #layout
        layout = [
            [sg.Text(self.nomes)],
            [sg.Button('Deletar')]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()
    
    def iniciar(self):
        tela = TelaListar()
        return tela.iniciar()
