#cálculo da próxima dose
#listar vacinas que o paciente precisa tomar
from visao.tela_vacinacao import TelaVacinacao
from modelo.vacinacao import Vacinacao
from datetime import datetime


class ControladorVacinacao():
  def __init__(self, controlador_paciente, controlador_vacina):
    self.__doses = []
    self.__vacinacao = []
    self.__tela_vacinacao = TelaVacinacao()
    self.__controlador_paciente = controlador_paciente
    self.__controlador_vacina = controlador_vacina

  
  def registrar_vacinacao (self):
    dados_vacinacao = self.__tela_vacinacao.pega_dados()
    data_de_vacinacao = datetime.strptime(dados_vacinacao["data_de_vacinacao"], "%d/%m/%Y")
    vacinacao = Vacinacao(dados_vacinacao ["cpf"], data_de_vacinacao, dados_vacinacao["vacina"], dados_vacinacao["dose"])
    self.__vacinacao.append(vacinacao)

    self.__tela_vacinacao.mostra_mensagem("Cadastrado com sucesso!")
    

  def lista_vacinacao(self):
    if len(self.__vacinacao)!=0:
        cpf = self.__tela_vacinacao.pegar_cpf()
        for vacinacao in self.__vacinacao:
            if vacinacao.cpf == cpf:
              self.__tela_vacinacao.mostra_vacinacao(vacinacao.data_de_vacinacao,
                                                     vacinacao.vacina,
                                                     vacinacao.dose)
    else:
      self.__tela_vacinacao.mostra_mensagem("Atenção: não existem vacinas aplicadas")