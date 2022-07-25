from excecoes.valor_invalido import ValorInvalido
import PySimpleGUI as sg


class TelaEnfermeiro:
  def __init__(self):
    self.__window = None

  def mostra_tela_login(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('Por favor, informe os seus dados:', font=("Helvica", 25))],
      [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
      [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='senha')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    button, values = self.open()
    email = values['email']
    senha = values['senha']
    self.close()
    return {"email": email, "senha": senha}

  def mostra_mensagem (self, mensagem: str):
    sg.popup('', mensagem)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
  
  
  def mostra_tela_opcoes(self):
    layout = [
      [sg.Text('Área de pacientes', font=("Helvica", 15))],
      [sg.Radio('Incluir paciente', "RD1", key='1')],
      [sg.Radio('Listar pacientes', "RD1", key='2')],
      [sg.Radio('Excluir paciente', "RD1", key='3')],
      [sg.Radio('Sair', "RD1", key='0')],
      [sg.Text('Área de vacinas', font=("Helvica", 15))],
      [sg.Radio('Incluir Vacina', "RD1", key='4')],
      [sg.Radio('Listar Vacinas', "RD1", key='5')],
      [sg.Radio('Alterar Vacina', "RD1", key='6')],
      [sg.Radio('Excluir Vacina', "RD1", key='7')],
      [sg.Text('Área de doses', font=("Helvica", 15))],
      [sg.Radio('Incluir dose', "RD1", key='8')],
      [sg.Radio('Listar doses', "RD1", key='9')],
      [sg.Text('Área de vacinação', font=("Helvica", 15))],
      [sg.Radio('Registrar vacinação', "RD1", key='10')],
      [sg.Radio('Listar vacinação', "RD1", key='11')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    button, values = self.open()
    self.close()
    opcao = 0
    if values['1']:
      opcao = 1
    elif values['2']:
      opcao = 2
    elif values['3']:
      opcao = 3
    elif values['4']:
      opcao = 4
    elif values['5']:
      opcao = 5
    elif values['6']:
      opcao = 6
    elif values['7']:
      opcao = 7
    elif values['8']:
      opcao = 8
    elif values['9']:
      opcao = 9
    elif values['10']:
      opcao = 10
    elif values['11']:
      opcao = 11
    elif values['0']:
      opcao = 0
    if button in (None, 'Cancelar'):
      opcao = 0
    return opcao

