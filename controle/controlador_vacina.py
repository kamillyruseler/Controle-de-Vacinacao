from modelo.vacina import Vacina
from visao.tela_vacina import TelaVacina
from modelo.dose import Dose
from visao.tela_dose import TelaDose
from excecoes.valor_invalido import ValorInvalido

class ControladorVacina():

  def __init__(self):
    self.__vacinas = []
    self.__doses = []
    self.__tela_vacina = TelaVacina()
    self.__tela_dose = TelaDose()

  def pega_vacina_por_doenca (self, doenca: str):
    for vacina in self.__vacinas:
      if (vacina.doenca == doenca):
        return vacina
    return None

  def incluir_vacina(self):
    try:
      dados_vacina = self.__tela_vacina.pega_dados()
    except ValorInvalido:
      return self.__tela_vacina.mostra_mensagem("Valor inválido. Digite um número inteiro")
    if dados_vacina == 0:
      return
    vacina = Vacina(dados_vacina["doenca"], dados_vacina["faixa_etaria_inicial"], dados_vacina["faixa_etaria_final"])
    existe = False
    for vacina in self.__vacinas:
      if vacina.doenca == dados_vacina["doenca"]:
        existe = True
        self.__tela_vacina.mostra_mensagem("Erro. Já existe uma vacina come esse nome")
    if not existe:
      self.__vacinas.append(vacina)
      self.__tela_vacina.mostra_mensagem("Cadastrado com sucesso!")

  def alterar_vacina(self):
    self.lista_vacinas()

    if (len(self.__vacinas)) != 0:
      doenca = self.__tela_vacina.seleciona_vacina()
      if doenca == 0:
        return
      vacina = self.pega_vacina_por_doenca(doenca)

      if(vacina is not None):
        try:
          novos_dados_vacina = self.__tela_vacina.pega_dados()
        except ValorInvalido:
          return self.__tela_vacina.mostra_mensagem("Valor inválido. Digite um número inteiro")
        if novos_dados_vacina == 0:
          return
        vacina.doenca = novos_dados_vacina["doenca"]
        vacina.faixa_etaria_inicial = novos_dados_vacina["faixa_etaria_inicial"]
        vacina.faixa_etaria_final = novos_dados_vacina["faixa_etaria_final"]
        self.lista_vacinas()
      else:
        self.__tela_vacina.mostra_mensagem("ATENCAO: Vacina não existente")

  def lista_vacinas(self):
    if len(self.__vacinas)!=0:
      vacinas = []
      for vacina in self.__vacinas:
        doses = []
        for dose in self.__doses:
          if (dose.doenca == vacina.doenca):
            doses.append({"lote": dose.lote})
        vacinas.append({"doenca": vacina.doenca, "faixa_etaria_inicial": vacina.faixa_etaria_inicial, "faixa_etaria_final": vacina.faixa_etaria_final, "doses": doses})
      self.__tela_vacina.mostra_vacinas(vacinas)
    else:
      self.__tela_vacina.mostra_mensagem("Atenção: não existem vacinas cadastradas")

  def excluir_vacina(self):
    
    self.lista_vacinas()
    if len(self.__vacinas)!=0:
      doenca = self.__tela_vacina.seleciona_vacina()
      if doenca == 0:
        return
      vacina = self.pega_vacina_por_doenca(doenca)

      if (vacina is not None):
        self.__vacinas.remove(vacina)
        self.lista_vacinas()
      else:
        self.__tela_vacina.mostra_mensagem("ATENÇÃO: vacina não existente")


  def incluir_dose(self):
    dados_dose = self.__tela_dose.pega_dados()
    if dados_dose == 0:
      return
    dose = Dose(dados_dose["doenca"], dados_dose["lote"])
    existe = False

    for vacina in self.__vacinas:
      if (vacina.doenca == dados_dose["doenca"]):
        existe = True
        self.__doses.append(dose)
        self.__tela_dose.mostra_mensagem("Cadastrado com sucesso!")
    if not existe:
      self.__tela_dose.mostra_mensagem("Erro. Não existe nenhuma vacina com esse nome")

  def lista_doses(self):
      if len(self.__doses)!=0:
        doses = []
        for dose in self.__doses:
          doses.append({"doenca": dose.doenca, "lote": dose.lote})
        self.__tela_dose.mostra_doses(doses)
      else:
        self.__tela_dose.mostra_mensagem("Atenção: não existem doses cadastradas")
