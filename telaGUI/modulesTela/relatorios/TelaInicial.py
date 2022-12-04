import PySimpleGUI as sg
from telaGUI.modulesTela.relatorios.TelaCadastrar import TelaCadastrar

class TelaInicial:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('1: Totalização dos treinos de um aluno por avaliação')],
            [sg.Text('2: Avaliações de treino de um determinado professor')],
            [sg.Text('3: Exercícios de acordo com a sua função/agrupamento')],
            [sg.Text('4 :Totalização do gasto com professores')],
            [sg.Text('5: Aparelhos de acordo com sua quantidade e número de exercício em que é utilizado')],
            [sg.Text('6: Média de tempo para cada tipo de treino de um aluno')],
            [sg.Text('7: Voltar')],
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
            pass
        elif(escolha == '3'):
            pass
        elif(escolha == '4'):
            pass
        elif(escolha == '5'):
            return False
        print(self.values)
