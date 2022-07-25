from excecoes.cpf_incorreto import CpfIncorreto
from excecoes.valor_invalido import ValorInvalido
import PySimpleGUI as sg


class TelaPaciente:
  def __init__(self):
    self.__window = None

  def pega_dados(self):
    layout = [
      [sg.Text('Adicionar paciente', font=("Helvica", 25))],
      [sg.Text('Nome: '), sg.In(key='nome')],
      [sg.Text('CPF: '), sg.In(key='cpf')],
      [sg.Text('Data de nascimento (DD/MM/YYYY):: '), sg.In(key='data_de_nascimento')],
      [sg.Text('Telefone: '), sg.In(key='telefone')],
      [sg.Text('Nome do responsável: '), sg.In(key='nome_responsavel')],
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

    try:
      telefone = int(values['telefone'])
    except:
      raise ValorInvalido()
    return {"nome": values['nome'], "cpf": cpf, "data_de_nascimento": values['data_de_nascimento'], "telefone": telefone, "nome_responsavel": values['nome_responsavel']}

  def mostra_pacientes (self, dados_pacientes):
    column = []
    for dados_paciente in dados_pacientes:
      column.extend([
        [sg.Text('- - - -')],
        [sg.Text('Nome: ' + dados_paciente['nome'])],
        [sg.Text('CPF: ' + str(dados_paciente['cpf']))],
        [sg.Text('Data de nascimento: ' + str(dados_paciente['data_de_nascimento']))],
        [sg.Text('Telefone: ' + str(dados_paciente["telefone"]))],
        [sg.Text('Responsável: ' + dados_paciente['nome_responsavel'])],
      ])
    layout = [
      [sg.Text('Detalhes', font=("Helvica", 15))],
      [sg.Column(column, scrollable=True, vertical_scroll_only=True, size=(200, 250))],
      [sg.Button('Voltar')],
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    self.__window.Read()
    self.__window.close()

  def seleciona_paciente(self):
    layout = [
      [sg.Text('Selecionar paciente', font=("Helvica", 25))],
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

  def mostra_mensagem(self, mensagem: str):
    sg.popup('', mensagem)

  