from excecoes.valor_invalido import ValorInvalido
import PySimpleGUI as sg

class TelaEnfermeiro:
  def __init__(self):
    self.__window = None
    self.mostra_tela_login()

  def mostra_tela_login(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('Por favor, informe os seus dados:', font=("Helvica", 25))],
      [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
      [sg.Text('Senha:', size=(15, 1)), sg.InputText('', key='senha')]
      
    ]
    self.__window = sg.Window('Controle de vacinação').Layout(layout)
    button, values = self.open()
    email = values['email']
    senha = values['senha']
    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    self.close()
    return {"email": email, "senha": senha}

  def mostra_mensagem (self, mensagem: str):
    print (mensagem)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values
  
  
  def mostra_tela_opcoes(self):
    print("")
    print("*******")
    print ("Área de pacientes")
    print ("1 - Incluir paciente")
    print ("2 - Listar paciente")
    print ("3 - Excluir paciente")
    print ("0 - Sair")
    print("")
    print("Área de vacinas")
    print ("4 - Incluir Vacina")
    print ("5 - Listar Vacinas")
    print ("6 - Alterar Vacina")
    print ("7 - Excluir Vacina")
    print("")
    print("Área de doses")
    print ("8 - Incluir dose")
    print ("9 - Listar doses")
    print("")
    print("Área de vacinação")
    print ("10 - Registrar vacinação")
    print ("11 - Listar vacinação")
    print("*******")
    while True:
      try:
        opcao = int(input("Opção: "))
        if opcao > 11 or opcao < 0:
          raise ValorInvalido()
        break
      except:
        raise ValorInvalido()
    return opcao

