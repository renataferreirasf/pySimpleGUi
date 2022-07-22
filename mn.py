import PySimpleGUI as sg

class Mn:
    def __init__(self):
        layout = [
            [sg.Text('Name'), sg.Input(key='name')],
            [sg.Text('Age'), sg.Input(key='Age')],
            [sg.Text('Providers?'), sg.Input()],
            [sg.Checkbox('Gmail', key='Gmail'), sg.Checkbox('Outlook', key='Outlook'), sg.Checkbox('Yahoo', key='Yahoo')],
            [sg.Button('Send')]
        ]

        janela = sg.Window("Dados do Unsuário").layout(layout)
        self.button, self.values = janela.Read()

    def Start(self):
        print(self.values)
tela = Mn()
tela.Start()