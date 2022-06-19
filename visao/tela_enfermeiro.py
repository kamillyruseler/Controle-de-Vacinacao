

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
    print ("Área de pacientes")
    print ("1 - Incluir paciente")
    print ("2 - Listar paciente")
    print ("3 - Excluir paciente")
    print ("4 - Alterar paciente")
    print ("0 - Sair")
    print("")
    print("Área de vacinas")
    print ("5 - Incluir Vacina")
    print ("6 - Listar Vacinas")
    print ("7 - Alterar Vacina")
    print ("8 - Excluir Vacina")
    opcao = int(input("Opção: "))
    return opcao

