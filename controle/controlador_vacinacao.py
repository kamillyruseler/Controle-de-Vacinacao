#cálculo da próxima dose
#listar vacinas que o paciente precisa tomar
from modelo.vacina import Vacina
from visao.tela_vacinacao import TelaVacinacao
from modelo.paciente import Paciente
from modelo.dose import Dose
from modelo.vacinacao import Vacinacao
from controle.controlador_paciente import ControladorPaciente
from controle.controlador_vacina import ControladorVacina


class ControladorVacinacao():
  def __init__(self):
    
    self.__doses = []
    self.__vacinacao = []
    self.__tela_vacinacao = TelaVacinacao()
    self.__controlador_paciente = ControladorPaciente()
    self.__controlador_vacina = ControladorVacina()
    self.__pacientes = Paciente

  def registrar_vacinacao (self):
    dados_vacinacao = self.__tela_vacinacao.pega_dados()
    vacinacao = Vacinacao(dados_vacinacao ["cpf"], dados_vacinacao["data_de_vacinacao"], dados_vacinacao["vacina"], dados_vacinacao["dose"])
    self.__vacinacao.append(vacinacao)

    self.__tela_vacinacao.mostra_mensagem("Cadastrado com sucesso!")
    


  def lista_vacinacao(self):
    if len(self.__vacinacao)!=0:
        for vacinacao in self.__vacinacao:
          print("teste")

    else:
      self.__tela_vacinacao.mostra_mensagem("Atenção: não existem vacinas aplicadas")