import PySimpleGUI as sg


class Mn:
    def __init__(self):
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button()]
        ]

        janela = sg.Window("Dados do Unsuário").layout(layout)
        self.button, sefl.values