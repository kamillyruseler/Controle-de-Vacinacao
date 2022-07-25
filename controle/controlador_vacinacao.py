from visao.tela_vacinacao import TelaVacinacao
from modelo.vacinacao import Vacinacao
from datetime import datetime
from excecoes.cpf_incorreto import CpfIncorreto


class ControladorVacinacao():
  def __init__(self, controlador_paciente, controlador_vacina):
    self.__doses = []
    self.__vacinacao = []
    self.__pacientes = []
    self.__vacinas = []
    self.__tela_vacinacao = TelaVacinacao()
    self.__controlador_paciente = controlador_paciente
    self.__controlador_vacina = controlador_vacina

  
  def registrar_vacinacao (self):
    try:
        dados_vacinacao = self.__tela_vacinacao.pega_dados()
    except CpfIncorreto:
        self.__tela_vacinacao.mostra_mensagem("CPF incorreto!")
        return self.registrar_vacinacao()
    if dados_vacinacao == 0:
        return
    try:
        data_de_vacinacao = datetime.strptime(dados_vacinacao["data_de_vacinacao"], "%d/%m/%Y")
    except:
        self.__tela_vacinacao.mostra_mensagem("Data em formato incorreto")
        return self.registrar_vacinacao()
    vacinacao = Vacinacao(dados_vacinacao ["cpf"], data_de_vacinacao, dados_vacinacao["vacina"], dados_vacinacao["dose"])
    self.__vacinacao.append(vacinacao)
    self.__tela_vacinacao.mostra_mensagem("Cadastrado com sucesso!")
    

  def lista_vacinacao(self):
    if len(self.__vacinacao)!=0:
        try:
          cpf = self.__tela_vacinacao.pegar_cpf()
        except CpfIncorreto:
          self.__tela_vacinacao.mostra_mensagem("CPF incorreto!")
          return self.lista_vacinacao()
        if cpf == -1:
          return
        vacinacoes = []
        for vacinacao in self.__vacinacao:
          if vacinacao.cpf == cpf:
            vacinacoes.append(vacinacao)
        self.__tela_vacinacao.mostra_vacinacao(vacinacoes)
    else:
      self.__tela_vacinacao.mostra_mensagem("Atenção: não existem vacinas aplicadas")