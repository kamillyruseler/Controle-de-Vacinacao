from excecoes.valor_invalido import ValorInvalido
import PySimpleGUI as sg


class TelaVacina:
  def __init__(self):
    self.__window = None

  def pega_dados(self):
    layout = [
      [sg.Text('Adicionar vacina', font=("Helvica", 25))],
      [sg.Text('Doença/nome: '), sg.In(key='nome')],
      [sg.Text('Faixa etária inicial em meses (número inteiro): '), sg.In(key='faixa_etaria_inicial')],
      [sg.Text('Faixa etária FINAL em meses (número inteiro): '), sg.In(key='faixa_etaria_final')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    button, values = self.__window.Read()
    self.__window.close()
    if button in (None, 'Cancelar'):
      return 0
    try:
      faixa_etaria_inicial = int(values['faixa_etaria_inicial'])
      faixa_etaria_final = int(values['faixa_etaria_final'])
    except:
      raise ValorInvalido()

    return {"doenca": values['nome'], "faixa_etaria_inicial": faixa_etaria_inicial, "faixa_etaria_final": faixa_etaria_final}

  def mostra_vacinas(self, dados_vacinas):
    column = []
    for dados_vacina in dados_vacinas:
      column.extend([
        [sg.Text('- - - -')],
        [sg.Text('Doença/nome da vacina: ' + dados_vacina["doenca"])],
        [sg.Text('Faixa etária inicial (meses): ' + str(dados_vacina["faixa_etaria_inicial"]))],
        [sg.Text('Faixa etária FINAL (meses): ' + str(dados_vacina["faixa_etaria_final"]))],
      ])
      if dados_vacina['doses']:
        column.append([sg.Text('Doses:')])
      for dose in dados_vacina['doses']:
        column.append([sg.Text(' Lote: ' + dose['lote'])])
    layout = [
      [sg.Text('Detalhes', font=("Helvica", 15))],
      [sg.Column(column, scrollable=True, vertical_scroll_only=True, size=(200, 250))],
      [sg.Button('Voltar')],
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    self.__window.Read()
    self.__window.close()

  def seleciona_vacina(self):
    layout = [
      [sg.Text('Seleciona vacina', font=("Helvica", 25))],
      [sg.Text('Doenca/nome: '), sg.In(key='doenca')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    button, values = self.__window.Read()
    self.__window.close()
    if button in (None, 'Cancelar'):
      return 0
    return values['doenca']

  def mostra_mensagem(self, mensagem: str):
    sg.popup('', mensagem)