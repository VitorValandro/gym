import PySimpleGUI as sg
from PySimpleGUI import Window

from telaGUI.modulesTela.aluno.TelaCadastrar import TelaCadastrar
from telaGUI.modulesTela.aluno.TelaEditar import TelaEditar
from telaGUI.modulesTela.aluno.TelaListar import TelaListar
from telaGUI.modulesTela.aluno.TelaDelete import TelaDelete


class TelaInicial:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('1: Cadastrar um aluno')],
            [sg.Text('2: Editar um aluno')],
            [sg.Text('3: Listar alunos')],
            [sg.Text('4 :Deletar um aluno')],
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
            pass
            tela = TelaDelete()
            tela.iniciar()
        elif(escolha == '5'):
            Window.close()
            return False
        print(self.values)
