import PySimpleGUI as sg
from telaGUI.modulesTela.aparelho.TelaCadastrarAparelho2 import TelaCadastrarAparelho2


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
            tela = TelaCadastrarAparelho2()
            tela.iniciar()
        elif(escolha == '2'):
            pass
        elif(escolha == '3'):
            pass
        elif(escolha == '4'):
            pass
        elif(escolha == '5'):
            pass
        print(self.values)
