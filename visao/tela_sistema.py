

class TelaSistema:
  def __init__(self):
    pass
  
  def mostrar_menu_inicial(self):
    print("Bem-vindo a tela inicial")
    print ("")
    print ("Digite 1 para realizar o seu login")
    print ("Digite 0 para sair")
    while True:
      try:
        opcao = int(input("Opção: "))
        break
      except:
        print ("Valor inválido. Digite 1 ou 0")
    return opcao
