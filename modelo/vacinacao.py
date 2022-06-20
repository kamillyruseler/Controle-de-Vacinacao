from datetime import date

#revendo necessidade do código de vacinação

#(dados_vacinacao ["cpf"], dados_vacinacao["data_de_vacinacao"], dados_vacinacao["doenca"], dados_vacinacao["dose"])

class Vacinacao():
  def __init__(self, cpf: int, data_de_vacinacao: date, vacina: str, dose: str):
    if isinstance (data_de_vacinacao, date):
      self.__data_de_vacinacao = data_de_vacinacao
    if isinstance(cpf, int):
        self.__cpf = cpf
    if isinstance(vacina, str):
        self.__vacina = vacina
    if isinstance(dose, str):
        self.__dose = dose
    self.__vacinas = []

  #lista de vacinas para gerar relatório
  
  @property
  def dose(self):
    return self.__dose
  
  @dose.setter
  def dose (self, dose: str):
    if isinstance (dose, str):
      self.__dose = dose

  
  @property
  def vacina(self):
    return self.__vacina
  
  @vacina.setter
  def vacina (self, vacina: str):
    if isinstance (vacina, str):
      self.__vacina = vacina

  
  @property
  def cpf(self):
    return self.__cpf
  
  @cpf.setter
  def cpf (self, cpf: int):
    if isinstance (cpf, int):
      self.__cpf = cpf
  
  
  @property
  def vacinas (self):
    return self.__vacinas
  
  @property
  def data_de_vacinacao(self):
    return self.__data_de_vacinacao
  
  @data_de_vacinacao.setter
  def data_de_vacinacao (self, data_de_vacinacao: date):
    if isinstance (data_de_vacinacao, date):
      self.__data_de_vacinacao = data_de_vacinacao
