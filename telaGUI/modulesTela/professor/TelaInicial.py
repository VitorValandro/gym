import PySimpleGUI as sg
from telaGUI.modulesTela.professor.TelaCadastrar import TelaCadastrar
from telaGUI.modulesTela.professor.TelaEditar import TelaEditar
from telaGUI.modulesTela.professor.TelaListar import TelaListar
from telaGUI.modulesTela.professor.TelaDelete import TelaDelete


class TelaInicial:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('1: Cadastrar um professor')],
            [sg.Text('2: Editar um professor')],
            [sg.Text('3: Listar professor')],
            [sg.Text('4 :Deletar um professor')],
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
        print(self.values)
