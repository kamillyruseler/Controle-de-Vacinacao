from excecoes.cpf_incorreto import CpfIncorreto
import PySimpleGUI as sg


class TelaVacinacao:
    def __init__(self):
        self.__window = None

    def pega_dados(self):
        layout = [
            [sg.Text('Adicionar vacinação', font=("Helvica", 25))],
            [sg.Text('CPF: '), sg.In(key='cpf')],
            [sg.Text('Data de vacinação (DD/MM/YYYY):: '), sg.In(key='data_de_vacinacao')],
            [sg.Text('Nome da vacina/doença: '), sg.In(key='vacina')],
            [sg.Text('Código do lote: '), sg.In(key='dose')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controle de vacinação').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        if button in (None, 'Cancelar'):
            return 0
        try:
            cpf = int(values['cpf'])
        except:
            raise CpfIncorreto()

        return {
            "cpf": cpf,
            "data_de_vacinacao": values['data_de_vacinacao'],
            "vacina": values['vacina'],
            "dose": values['dose']
        }

    def mostra_mensagem(self, mensagem: str):
        sg.popup('', mensagem)

    def mostra_vacinacao(self, vacinacoes):
        column = []
        for vacinacao in vacinacoes:
            column.extend([
                [sg.Text('- - - -')],
                [sg.Text('Data: ' + str(vacinacao.data_de_vacinacao))],
                [sg.Text('Doença/nome da vacina: ' + vacinacao.vacina)],
                [sg.Text('Lote: ' + vacinacao.dose)],
            ])
        layout = [
            [sg.Text('Detalhes', font=("Helvica", 15))],
            [sg.Column(column, scrollable=True, vertical_scroll_only=True, size=(200, 250))],
            [sg.Button('Voltar')],
        ]
        self.__window = sg.Window('Controle de vacinação').Layout(layout)
        self.__window.Read()
        self.__window.close()

    def pegar_cpf(self):
        layout = [
            [sg.Text('Selecionar vacinação', font=("Helvica", 25))],
            [sg.Text('CPF: '), sg.In(key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controle de vacinação').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        if button in (None, 'Cancelar'):
            return -1
        try:
            cpf = int(values['cpf'])
        except:
            raise CpfIncorreto()
        return cpf