import PySimpleGUI as sg
from telaGUI.modulesTela.aparelho.TelaCadastrarAparelho2 import TelaCadastrarAparelho2


class TelaInicial:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('1: Cadastrar um exercicío')],
            [sg.Text('2: Editar um exercicío')],
            [sg.Text('3: Listar exercicíos')],
            [sg.Text('4 :Deletar um exercicío')],
            [sg.Text('5: Voltar')],
            [sg.Button('Enviar'), sg.Input(size=3, key="escolha")]
        ]
        #janela
        janela = sg.Window("Dados gerais").layout(layout)
        #extrair dados
        self.button, self.values = janela.Read()
    
    def iniciar(self):
        escolha = self.values['escolha']
        if(escolha == '1'):
            pass
        elif(escolha == '2'):
            pass
        elif(escolha == '3'):
            pass
        elif(escolha == '4'):
            pass
        elif(escolha == '5'):
            pass
        print(self.values)
