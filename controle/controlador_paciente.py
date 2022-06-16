from visao.tela_paciente import TelaPaciente
from modelo.paciente import Paciente
from datetime import datetime

class ControladorPaciente():

  def __init__(self):
    self.__pacientes = []
    self.__tela_paciente = TelaPaciente()

  def selecionar_paciente(self, cpf: int):
    for paciente in self.__pacientes:
      if(paciente.cpf == cpf):
        return paciente
    return None

  def inclui_paciente(self):
    dados_paciente = self.__tela_paciente.pega_dados()
    data_de_nascimento = datetime.strptime(dados_paciente["data_de_nascimento"], "%d/%m/%Y")
    paciente = Paciente(dados_paciente["nome"],dados_paciente["cpf"], data_de_nascimento, dados_paciente["telefone"], dados_paciente["nome_responsavel"])
    self.__pacientes.append(paciente)

  def lista_pacientes(self):
    for paciente in self.__pacientes:
      self.__tela_paciente.mostra_paciente({"nome": paciente.nome, "cpf": paciente.cpf, "data_de_nascimento": paciente.data_de_nascimento, "telefone": paciente.telefone, "nome_responsavel": paciente.nome_responsavel})

  def altera_paciente(self):
    self.lista_pacientes()
    cpf_paciente = self.__tela_paciente.seleciona_paciente()
    paciente = self.pega_paciente_por_cpf(cpf_paciente)

    if (paciente is not None):
      novos_dados = self.__tela_paciente.pega_dados()
      paciente.nome = novos_dados["nome"]
      paciente.cpf = novos_dados["cpf"]
      paciente.data_de_nascimento = novos_dados["data_de_nascimento"]
      paciente.telefone = novos_dados["telefone"]
      paciente.nome_responsavel = novos_dados["nome_responsavel"]
      self.lista_pacientes()
    else:
      self.__tela_paciente.mostra_mensagem("ATENCAO: não existente")

  def pega_paciente_por_cpf(self, cpf: int):
    for paciente in self.__pacientes:
      if (paciente.cpf == cpf):
        return paciente
    return None

  def excluir_paciente(self):
    self.lista_pacientes()
    cpf_paciente = self.__tela_paciente.seleciona_paciente()
    paciente = self.pega_paciente_por_cpf(cpf_paciente)

    if(paciente is not None):
      self.__pacientes.remove(paciente)
      self.lista_pacientes()
    else:
      self.__tela_paciente.mostra_mensagem("ATENCAO: não existente")

    #falta método de retornar e abrir menu novamente
    