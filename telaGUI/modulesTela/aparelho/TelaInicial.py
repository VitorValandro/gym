import PySimpleGUI as sg
from telaGUI.modulesTela.aparelho.TelaCadastrar import TelaCadastrar
from telaGUI.modulesTela.aparelho.TelaEditar import TelaEditarAparelho
from telaGUI.modulesTela.aparelho.TelaDelete import TelaDeleteAparelho
from telaGUI.modulesTela.aparelho.TelaListar import TelaListarAparelho



class TelaInicial:
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
        escolha = self.values['escolha']
        if(escolha == '1'):
            tela = TelaCadastrar()
            tela.iniciar()
        elif(escolha == '2'):
            tela = TelaEditarAparelho()
            tela.iniciar()
        elif(escolha == '3'):
            tela = TelaListarAparelho()
            tela.iniciar()
        elif(escolha == '4'):
            tela = TelaDeleteAparelho()
            tela.iniciar()
        elif(escolha == '5'):
            return False
