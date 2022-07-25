from visao.tela_paciente import TelaPaciente
from modelo.paciente import Paciente
from datetime import datetime
from dateutil.relativedelta import relativedelta
from excecoes.cpf_incorreto import CpfIncorreto
from excecoes.valor_invalido import ValorInvalido
#pip install python-dateutil


class ControladorPaciente:

  def __init__(self):
    self.__pacientes = []
    self.__tela_paciente = TelaPaciente()

  
  def inclui_paciente(self):
    try:
      dados_paciente = self.__tela_paciente.pega_dados()
    except CpfIncorreto:
      self.__tela_paciente.mostra_mensagem("CPF incorreto!")
      return self.inclui_paciente()
    except ValorInvalido:
      self.__tela_paciente.mostra_mensagem("Valor inválido. Digite um número inteiro, sem caracteres")
      return self.inclui_paciente()
    if dados_paciente == 0:
      return
    try:
      data_de_nascimento = datetime.strptime(dados_paciente["data_de_nascimento"], "%d/%m/%Y")
    except:
      self.__tela_paciente.mostra_mensagem("Data em formato incorreto")
      return self.inclui_paciente()
    paciente = Paciente(dados_paciente["nome"],dados_paciente["cpf"], data_de_nascimento, dados_paciente["telefone"], dados_paciente["nome_responsavel"])
    existe = False
    for paciente in self.__pacientes:
      if (paciente.cpf == dados_paciente["cpf"]):
        existe = True
        self.__tela_paciente.mostra_mensagem("Erro. Já existe um paciente com esse CPF")
    if not existe:
      self.__pacientes.append(paciente)
      self.__tela_paciente.mostra_mensagem("Cadastrado com sucesso!")
      self.calcular_idade(data_de_nascimento)
      
    

  def calcular_idade(self, data_de_nascimento):
    d2 = datetime.now()
    diferenca =  relativedelta(d2, data_de_nascimento)
    self.__tela_paciente.mostra_mensagem(("{} ano(s), {} mes(es), {} dias"
       .format(diferenca.years, diferenca.months, diferenca.days)))   
  
  def lista_pacientes(self):
    if len(self.__pacientes)!=0:
      pacientes = []
      for paciente in self.__pacientes:
        pacientes.append({"nome": paciente.nome, "cpf": paciente.cpf, "data_de_nascimento": paciente.data_de_nascimento, "telefone": paciente.telefone, "nome_responsavel": paciente.nome_responsavel})
      self.__tela_paciente.mostra_pacientes(pacientes)
    else:
      self.__tela_paciente.mostra_mensagem("Atenção: não existem pacientes cadastrados")


  def pega_paciente_por_cpf(self, cpf: int):
    for paciente in self.__pacientes:
      if (paciente.cpf == int(cpf)):
        return paciente
    return None

  def excluir_paciente(self):
    self.lista_pacientes()
    if (len(self.__pacientes)) != 0:
      while True:
        try:
          cpf_paciente = self.__tela_paciente.seleciona_paciente()
          break
        except CpfIncorreto:
          self.__tela_paciente.mostra_mensagem("CPF incorreto!")
          pass
      if cpf_paciente == -1:
        return
      paciente = self.pega_paciente_por_cpf(cpf_paciente)
  
      if(paciente is not None):
        self.__pacientes.remove(paciente)
        self.lista_pacientes()
        self.__tela_paciente.mostra_mensagem("Excluído com sucesso!")
      else:
        self.__tela_paciente.mostra_mensagem("Atenção: paciente não existe. Tente novamente.")
