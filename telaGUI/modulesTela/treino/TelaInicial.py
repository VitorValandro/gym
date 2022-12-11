import PySimpleGUI as sg
from telaGUI.modulesTela.treino.TelaCadastrar import TelaCadastrar
from telaGUI.modulesTela.treino.TelaEditar import TelaEditar
from telaGUI.modulesTela.treino.TelaListar import TelaListar
from telaGUI.modulesTela.treino.TelaDelete import TelaDelete


class TelaInicial:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('1: Cadastrar um treino')],
            [sg.Text('2: Editar um treino')],
            [sg.Text('3: Listar treinos')],
            [sg.Text('4 :Deletar um treino')],
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
            tela = TelaEditar()
            tela.iniciar()
        elif(escolha == '3'):
            tela = TelaListar()
            tela.iniciar()
        elif(escolha == '4'):
            tela = TelaDelete()
            tela.iniciar()
        elif(escolha == '5'):
            return False
