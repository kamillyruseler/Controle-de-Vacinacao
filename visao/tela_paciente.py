

class TelaPaciente():
  def tela_opcoes(self):
    print ("Área de Pacientes")
    print ("Escolha a opção")
    print ("1 - Inclui paciente")
    print ("2 - Altera paciente")
    print ("3 - Exclui paciente")
    print ("0 - Retornar")

    opcao = int(input("Escolha a opção: "))
    return opcao

  def pega_dados(self):
    print("Informe os dados: ")
    nome = input("Nome: ")
    cpf = int(input("CPF: "))
    data_de_nascimento = input("Data de nascimento (DD/MM/YYYY): ")
    telefone = int(input("Telefone: "))
    nome_responsavel = input("Nome do responsável: ")
    return {"nome": nome, "cpf": cpf, "data_de_nascimento": data_de_nascimento, "telefone": telefone, "nome_responsavel": nome_responsavel}

  def mostra_paciente (self, dados_paciente):
    print("Nome: ", dados_paciente["nome"])
    print("CPF: ", dados_paciente["cpf"])
    print("Data de nascimento: ", dados_paciente["data_de_nascimento"])
    print("Telefone: ", dados_paciente["telefone"])
    print("Responsável: ", dados_paciente["nome_responsavel"])
    print("\n")

  def seleciona_paciente(self):
    cpf = input("CPF que deseja selecionar: ")
    return cpf
    
  def mostra_mensagem (self, mensagem):
    print (mensagem)

  