import PySimpleGUI as sg

class TelaCadastrarAparelho:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Insira o nome do aparelho'), sg.Input(size=20, key="nome")],
            [sg.Text('Insira a quantidade do aparelho'), sg.Input(size=3, key="quantidade")],
            [sg.Text('Escolha o tipo do aparelho abaixo')],
            [sg.Radio('Fixos','RADIO1', key="1")],
            [sg.Radio('Extensoras/Flexoras','RADIO1', key="2")],
            [sg.Radio('Livres','RADIO1', key="3")],
            [sg.Radio('Halteres','RADIO1', key="4")],
            [sg.Radio('Cardiovasculares','RADIO1', key="5")],
            [sg.Radio('Cross','RADIO1', key="6")],
            [sg.Button('Enviar dados para cadastro')]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)
        print(self.values["1"])

tela = TelaCadastrarAparelho()
tela.iniciar()