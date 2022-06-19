

class TelaDose():

  def pega_dados(self):
    print("")
    print("Informe os dados: ")
    doenca = input("Doença: ")
    lote = str(input("Lote: "))
    print("")
    return {"doenca": doenca, "lote": lote}

  def mostra_dose(self, dados_dose):
    print("Doença: ", dados_dose["doenca"])
    print("Lote: ", dados_dose["lote"])
    print("")

  def mostra_dose_por_doenca(self, dados_dose):
    print("Lote: ", dados_dose["lote"])
    print("")
  
  def mostra_mensagem(self, msg):
    print(msg)