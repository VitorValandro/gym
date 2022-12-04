import PySimpleGUI as sg

class Trip:

    def __init__(self,nome,quantidade,tipo):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__tipo = tipo

    def __repr__(self):
        return f"nome:{self.__nome}, quantidade:{self.__quantidade}, tipo:{self.__tipo}"

trips=[Trip('Teste','2','Cross'),Trip('Qtars','4','Flex'),Trip('Legs','5','3')]

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 12))

layout = [[sg.Listbox(trips, size=(40, 3))]]
window = sg.Window('Title', layout, finalize=True)

while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(event, values)

window.close()