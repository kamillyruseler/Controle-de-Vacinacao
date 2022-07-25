import PySimpleGUI as sg


class TelaDose:
  def __init__(self):
    self.__window = None

  def pega_dados(self):
    layout = [
      [sg.Text('Adicionar dose', font=("Helvica", 25))],
      [sg.Text('Doença: '), sg.In(key='doenca')],
      [sg.Text('Lote: '), sg.In(key='lote')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    button, values = self.__window.Read()
    self.__window.close()

    if button in (None, 'Cancelar'):
      return 0
    return values

  def mostra_doses(self, dados_doses):
    column = []
    for dados_dose in dados_doses:
      column.extend([
        [sg.Text('- - - -')],
        [sg.Text('Doença: ' + dados_dose['doenca'])],
        [sg.Text('Lote: ' + dados_dose['lote'])],
      ])
    layout = [
      [sg.Text('Detalhes', font=("Helvica", 15))],
      [sg.Column(column, scrollable=True, vertical_scroll_only=True, size=(200, 250))],
      [sg.Button('Voltar')],
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    self.__window.Read()
    self.__window.close()

  def mostra_mensagem(self, mensagem: str):
    sg.popup('', mensagem)