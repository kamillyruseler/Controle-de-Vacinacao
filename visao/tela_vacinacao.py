

class TelaVacinacao():

  def pega_dados(self):
    print("")
    print("Informe os dados: ")
    cpf = int(input("CPF: "))
    data_de_vacinacao = input("Data de vacinação (DD/MM/YYYY): ")
    vacina = input("Nome da vacina: ")
    dose = input("Código do lote: ")
    print("")
    return {"cpf": cpf, "data_de_vacinacao": data_de_vacinacao, "vacina": vacina, "dose": dose}

  def mostra_mensagem (self, mensagem):
    print("")
    print (mensagem)
    print("")

  def mostra_vacinacao(self, data_de_vacinacao):
    print ("")
    print("Data: ", dados_vacinacao["data_de_vacinacao"])
    print("\n")