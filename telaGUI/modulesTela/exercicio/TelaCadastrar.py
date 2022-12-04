import PySimpleGUI as sg

class TelaCadastrar:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Insira o nome do Aluno'), sg.Input(size=20, key="nome")],
            [sg.Text('Insira o CPF'), sg.Input(size=3, key="cpf")],
            [sg.Text('Insira o peso'), sg.Input(size=3, key="peso")],
            [sg.Text('Insira a alutura'), sg.Input(size=3, key="altura")],
            [sg.Text('Insira o salário'), sg.Input(size=3, key="altura")],
            [sg.Text('Tipos de exercício abaixo')],
            [sg.Text('1- Braços', key="1"), sg.Text('2- Ombros', key="2"), sg.Text('3- Abdome', key="3")],
            [sg.Text('4- Pernas', key="4"), sg.Text('5- Cardio', key="5")],
            [sg.Text('Insira o tipo do exercicío'), sg.Input(size=3, key="tipo")],
            [sg.Text('Insira o ID do aparelho para este exercicío'), sg.Input(size=3, key="aparelho")],
            [sg.Button('Enviar dados para cadastro')]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

