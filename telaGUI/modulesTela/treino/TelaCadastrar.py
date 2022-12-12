import PySimpleGUI as sg

class TelaCadastrar:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Insira o nome do Treino'), sg.Input(size=20, key="nome")],
            [sg.Text('Insira o ID do aluno'), sg.Input(size=10, key="id_aluno")],
            [sg.Text('Insira o numero de repetições'), sg.Input(size=10, key="peso")],
            [sg.Text('Insira o peso do exercicio'), sg.Input(size=10, key="altura")],
            [sg.Text('Insira o id do exercicio'), sg.Input(size=10, key="altura")],
            [sg.Button('Enviar dados para cadastro')]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

