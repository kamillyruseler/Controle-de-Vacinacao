

class TelaEnfermeiro:
  def __init__(self):
    pass

  def mostra_tela_login(self):
    print ("Por favor, informe os seus dados:")
    email = input("Email: ")
    senha = input("Senha: ")
    return {"email": email, "senha": senha}

  def mostra_mensagem (self, mensagem: str):
    print (mensagem)

  def mostra_tela_opcoes(self):
    print ("O que você deseja fazer?")
    print ("1 - Incluir Paciente")
    print ("2 - Incluir Vacina")
    print ("0 - Retornar")
    opcao = int(input("Opção: "))
    return opcao