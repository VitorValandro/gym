import PySimpleGUI as sg

class TelaCadastrarAparelho2:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Insira o nome do aparelho'), sg.Input(size=20, key="nome")],
            [sg.Text('Insira a quantidade do aparelho'), sg.Input(size=3, key="quantidade")],
            [sg.Text('Escolha o tipo do aparelho abaixo')],
            [sg.Text('1- Fixos', key="1"), sg.Text('2- Extensoras/Flexoras', key="2"), sg.Text('3- Livres', key="3")],
            [sg.Text('4- Halteres', key="4"), sg.Text('5- Cardiovasculares', key="5"), sg.Text('6- Cross', key="6")],
            [sg.Text('Insira o tipo do aparelho'), sg.Input(size=3, key="tipo")],
            [sg.Button('Enviar dados para cadastro')]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)
        print(self.values["tipo"])
