from visao.tela_enfermeiro import TelaEnfermeiro
from modelo.enfermeiro import Enfermeiro
from controle.controlador_paciente import ControladorPaciente
import datetime 

#lista de enfermeiros autorizados no sistema

class ControladorEnfermeiro:
  def __init__(self):
    self.__enfermeiros = [Enfermeiro("nome", 1234567, datetime.datetime.now(), 4798840, "admin@gmail.com", "admin", 123)]
    self.__tela_enfermeiro = TelaEnfermeiro()
    self.__manter_tela = True

  def incluir(self):
    pass
  
  def retornar(self):
    exit(0)
  
  
  def logar(self):
    dados_enfermeiro = self.__tela_enfermeiro.mostra_tela_login()
    for enfermeiro in self.__enfermeiros:
      if (enfermeiro.email == dados_enfermeiro["email"]) and enfermeiro.senha == dados_enfermeiro["senha"]:
        self.__tela_enfermeiro.mostra_mensagem("Logado")
        return enfermeiro
      else:
        self.__tela_enfermeiro.mostra_mensagem("Senha inválida")
        return None

  
  def abre_tela_inicial(self):
    switcher = {0: self.retornar, 1: ControladorPaciente.incluir_paciente, 2: self.incluir}
    self.__manter_tela = True
    while self.__manter_tela:
      opcao_escolhida = self.__tela_enfermeiro.mostra_tela_opcoes()
      funcao_escolhida = switcher[opcao_escolhida]
      funcao_escolhida()
        