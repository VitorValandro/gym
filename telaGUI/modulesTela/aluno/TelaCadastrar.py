import PySimpleGUI as sg

class TelaCadastrar:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Insira o nome do Aluno'), sg.Input(size=20, key="nome")],
            [sg.Text('Insira o CPF'), sg.Input(size=10, key="cpf")],
            [sg.Text('Insira o peso'), sg.Input(size=10, key="peso")],
            [sg.Text('Insira a alutura'), sg.Input(size=10, key="altura")],
            [sg.Button('Enviar dados para cadastro')]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

