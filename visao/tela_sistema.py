import PySimpleGUI as sg

class TelaSistema:
  def __init__(self):
    self.__window = None
    self.init_components()
  
  def mostrar_menu_inicial(self):
    self.init_components()
    button, values = self.__window.Read()
    opcao = 0

    if values['1']:
      opcao = 1

    if values['0'] or button in(None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao

    def close(self):
      self.__window.Close()

  def init_components(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
          [sg.Text('Bem-vindo a tela inicial', font=("Helvica",25))],
          [sg.Text('Digite 1 para realizar o seu login ou 0 para sair', font=("Helvica",15))],
          [sg.Radio('Login',"RD1", key='1')],
          [sg.Radio('Finalizar sistema',"RD1", key='0')],
          [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      
    ]
    self.__window = sg.Window("Controle de vacinação").Layout(layout)
