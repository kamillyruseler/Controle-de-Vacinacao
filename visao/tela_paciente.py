

class TelaPaciente():

  def pega_dados(self):
    print("")
    print("Informe os dados: ")
    nome = input("Nome: ")
    while True:
      try:
        cpf = int(input("CPF: "))
        break
      except:
        print ("Valor inválido. Digite um número inteiro, sem caracteres")

    data_de_nascimento = input("Data de nascimento (DD/MM/YYYY): ")
    
    while True:
      try:
        telefone = int(input("Telefone: "))
        break
      except:
        print ("Valor inválido. Digite um número inteiro, sem caracteres")
    nome_responsavel = input("Nome do responsável: ")
    print("")
    return {"nome": nome, "cpf": cpf, "data_de_nascimento": data_de_nascimento, "telefone": telefone, "nome_responsavel": nome_responsavel}

  def mostra_paciente (self, dados_paciente):
    print("")
    print("Nome: ", dados_paciente["nome"])
    print("CPF: ", dados_paciente["cpf"])
    print("Data de nascimento: ", dados_paciente["data_de_nascimento"])
    print("Telefone: ", dados_paciente["telefone"])
    print("Responsável: ", dados_paciente["nome_responsavel"])
    print("")

  def seleciona_paciente(self):
    print("")
    cpf = input("CPF que deseja selecionar: ")
    print("")
    return cpf
    
  def mostra_mensagem (self, mensagem):
    print("")
    print (mensagem)
    print("")

  