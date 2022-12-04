import PySimpleGUI as sg

class TelaEditarAparelho:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Insira o nome do Aluno'), sg.Input(size=20, key="nome")],
            [sg.Text('Insira o CPF'), sg.Input(size=3, key="cpf")],
            [sg.Text('Insira o peso'), sg.Input(size=3, key="peso")],
            [sg.Text('Insira a alutura'), sg.Input(size=3, key="altura")],
            [sg.Text('Insira o salário'), sg.Input(size=3, key="altura")],
            [sg.Text('Escolha o turno do professor')],
            [sg.Text('1- Segunda Feira', key="1"), sg.Text('2- Terça Feira', key="2"), sg.Text('3- Quarta Feira', key="3")],
            [sg.Text('4- Quinta Feira', key="4"), sg.Text('5- Sexta Feira', key="5"), sg.Text('6- Sábado', key="6")],
            [sg.Text('Insira o dia de trabalho'), sg.Input(size=3, key="dia")],
            [sg.Text('1- Manhã', key="1"), sg.Text('2- Tarde', key="2"), sg.Text('3- Noite', key="3")],
            [sg.Text('Insira o turno do professor'), sg.Input(size=3, key="turno")],
            [sg.Button('Enviar dados para cadastro')]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)