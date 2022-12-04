import sqlite3
import PySimpleGUI as sg


conn = sqlite3.connect('info_auto.db')
query = ('''CREATE TABLE INFO_AUTO(
            ID INTEGER PRIMARY KEY,
            data_carico,
            marca_modello);''')
conn.execute(query)
conn.close()


def instert_data(data_carico, marca_modello):
    conn = sqlite3.connect('info_auto.db')
    c = conn.cursor()
    c.execute('INSERT INTO info_auto (data_carico, marca_modello) VALUES(?, ?)', (data_carico, marca_modello))
    conn.commit()
    c.close()


def retrieve_data():
    results = []
    conn = sqlite3.connect('info_auto.db')
    c = conn.execute('SELECT ID, data_carico, marca_modello FROM info_auto')
    for row in c:
        results.append(list(row))
    return results


def create():
    data_entry = retrieve_data()
    headings = ["DATA_CARICO", "MARCA_MODELLO"]

    dati_auto_layout = [
        [sg.Table(values=data_entry, headings=headings, max_col_width=35, auto_size_columns=True,
                  display_row_numbers=True,
                  select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                  justification='right',
                  enable_events=True,
                  key='-TABLE-',
                  tooltip='Parco veicoli')],
        [sg.Button('Exit'), sg.Button('Delete Row')]
    ]
    dati_auto_window = sg.Window("Gestione parco veicoli",
                                 dati_auto_layout,
                                 modal=True,
                                 resizable=True,
                                 finalize=True)

    while True:
        event, values = dati_auto_window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event == 'Delete Row':
            if values['-TABLE-'] == []:
                sg.popup('No Row Selected')
            else:
                if sg.popup_ok_cancel('Can not undo Delete: Continue?') == 'OK':
                    selected_index = values['-TABLE-'][0]
                    conn = sqlite3.connect('info_auto.db')
                    c = conn.cursor()
                    c.execute('DELETE from info_auto WHERE ID = ?', (selected_index,))
                    conn.commit()
                    c.close()

                    del data_entry[values['-TABLE-'][0]]
                    dati_auto_window['-TABLE-'].update(values=data_entry)

    dati_auto_window.close()


sg.theme('DarkRed1')

col_1 = [
    [sg.Text('DATI DI ARRIVO')],
    [sg.Text('Data ricevimento: ')],
    [sg.InputText(key='-DATA_CARICO-')],
    [sg.Text('Marca e Modello: ')],
    [sg.InputText(key='-MARCA_MODELLO-')],
    [sg.Push(), sg.Button('Submit'), sg.Button('Warehouse'), sg.Button('Exit')]]

layout = [[sg.Column(col_1)]]


window = sg.Window('Gestione parco veicoli',
                   layout,
                   enable_close_attempted_event=True,
                   resizable=True,
                   finalize=True)

while True:
    event, values = window.read()
    if (event == 'Exit' or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT) \
            and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
    elif event == 'Submit':
        instert_data(values['-DATA_CARICO-'], values['-MARCA_MODELLO-'])
        sg.popup('DATA UPLOADED')

    elif event == 'Warehouse':
        create()
window.close()