from visao.tela_enfermeiro import TelaEnfermeiro
from modelo.enfermeiro import Enfermeiro
from controle.controlador_paciente import ControladorPaciente
from controle.controlador_vacina import ControladorVacina
from visao.tela_dose import TelaDose
from controle.controlador_vacinacao import ControladorVacinacao
from excecoes.valor_invalido import ValorInvalido

class ControladorEnfermeiro:
  
  def __init__(self):
    self.__enfermeiros = [Enfermeiro("Enfermeiro teste", 1234567, 10/12/1998, 4798840, "a", "a", 123)] 
    self.__tela_enfermeiro = TelaEnfermeiro()
    self.__tela_dose = TelaDose()
    self.__manter_tela = True
    self.__controlador_paciente = ControladorPaciente()
    self.__controlador_vacina = ControladorVacina()
    self.__controlador_vacinacao = ControladorVacinacao(self.__controlador_paciente, self.__controlador_vacina)

  
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
    switcher = {0: self.retornar, 1: self.__controlador_paciente.inclui_paciente, 2: self.__controlador_paciente.lista_pacientes, 3: self.__controlador_paciente.excluir_paciente, 4: self.__controlador_vacina.incluir_vacina, 5: self.__controlador_vacina.lista_vacinas, 6: self.__controlador_vacina.alterar_vacina, 7: self.__controlador_vacina.excluir_vacina, 8: self.__controlador_vacina.incluir_dose, 9: self.__controlador_vacina.lista_doses, 10: self.__controlador_vacinacao.registrar_vacinacao, 11: self.__controlador_vacinacao.lista_vacinacao}
    self.__manter_tela = True
    while self.__manter_tela:
      try:
        opcao_escolhida = self.__tela_enfermeiro.mostra_tela_opcoes()
      except ValorInvalido:
        self.__tela_enfermeiro.mostra_mensagem('Valor inválido')
        return self.abre_tela_inicial()
      funcao_escolhida = switcher[opcao_escolhida]
      funcao_escolhida()
      