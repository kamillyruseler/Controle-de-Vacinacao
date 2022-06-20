

class TelaEnfermeiro:
  def __init__(self):
    pass

  def mostra_tela_login(self):
    print("\n")
    print ("Por favor, informe os seus dados:")
    email = input("Email: ")
    senha = input("Senha: ")
    print("")
    return {"email": email, "senha": senha}

  def mostra_mensagem (self, mensagem: str):
    print (mensagem)

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
        break
      except:
        print ("Valor inválido. Digite um número de 0 a 12")
    return opcao

