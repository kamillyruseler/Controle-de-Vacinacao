

class TelaVacina():
  def pega_dados(self):
    print("")
    print("Informe os dados: ")
    doenca = input("Doença: ")

    while True:
      try:     
        faixa_etaria_inicial = int(input("Faixa etária inicial em meses (número inteiro): "))
        break
      except:
        print ("Valor inválido. Digite um número inteiro")

    while True:
      try:
        faixa_etaria_final = int(input("Faixa etária FINAL em meses (número inteiro): "))
        break
      except:
        print ("Valor inválido. Digite um número inteiro")
        
    print("")
    return {"doenca": doenca, "faixa_etaria_inicial": faixa_etaria_inicial, "faixa_etaria_final": faixa_etaria_final}

  def mostra_vacina(self, dados_vacina):
    print ("")
    print("Doença: ", dados_vacina["doenca"])
    print("Faixa etária inicial (meses): ", dados_vacina["faixa_etaria_inicial"])
    print("Faixa etária FINAL (meses): ", dados_vacina["faixa_etaria_final"])
    print("\n")

  def seleciona_vacina(self):
    doenca = input("Doença que deseja selecionar: ")
    return doenca

  def mostra_mensagem(self, msg):
    print(msg)