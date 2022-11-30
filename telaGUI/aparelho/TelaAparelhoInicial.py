import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('1: Cadastrar um aparelho')],
            [sg.Text('2: Editar um aparelho')],
            [sg.Text('3: Listar aparelhos')],
            [sg.Text('4 :Deletar um aparelho')],
            [sg.Text('5: Voltar')],
            [sg.Button('Enviar'), sg.Input(size=3, key="escolha")]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()
    
    def iniciar(self):
        print(self.values)

tela = TelaPython()
tela.iniciar()