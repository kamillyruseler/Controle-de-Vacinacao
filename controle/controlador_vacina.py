from modelo.vacina import Vacina
from visao.tela_vacina import TelaVacina


class ControladorVacina():

  def __init__(self):
    self.__vacinas = []
    self.__tela_vacina = TelaVacina()

  def pega_vacina_por_doenca (self, doenca: str):
    for vacina in self.__vacinas:
      if (vacina.doenca == doenca):
        return vacina
    return None

  def incluir_vacina(self):
    dados_vacina = self.__tela_vacina.pega_dados()
    vacina = Vacina(dados_vacina["doenca"], dados_vacina["faixa_etaria_inicial"], dados_vacina["faixa_etaria_final"])
    self.__vacinas.append(vacina)
    self.__tela_vacina.mostra_mensagem("Cadastrado com sucesso!")

  def alterar_vacina(self):
    self.lista_vacinas()
    doenca = self.__tela_vacina.seleciona_vacina()
    vacina = self.pega_vacina_por_doenca(doenca)

    if(vacina is not None):
      novos_dados_vacina = self.__tela_vacina.pega_dados()
      vacina.doenca = novos_dados_vacina["doenca"]
      vacina.faixa_etaria_inicial = novos_dados_vacina["faixa_etaria_inicial"]
      vacina.faixa_etaria_final = novos_dados_vacina["faixa_etaria_final"]
      self.lista_vacinas()
    else:
      self.__tela_vacina.mostra_mensagem("ATENCAO: Vacina não existente")

  def lista_vacinas(self):
    if len(self.__vacinas)!=0:
      for vacina in self.__vacinas:
        self.__tela_vacina.mostra_vacina({"doenca": vacina.doenca, "faixa_etaria_inicial": vacina.faixa_etaria_inicial, "faixa_etaria_final": vacina.faixa_etaria_final})
    else:
      self.__tela_vacina.mostra_mensagem("Atenção: não existem vacinas cadastradas")

  def excluir_vacina(self):
    self.lista_vacinas()
    doenca = self.__tela_vacina.seleciona_vacina()
    vacina = self.pega_vacina_por_doenca(doenca)

    if(vacina is not None):
      self.__vacinas.remove(vacina)
      self.lista_vacinas()
    else:
      self.__tela_vacina.mostra_mensagem("ATENÇÃO: vacina não existente")