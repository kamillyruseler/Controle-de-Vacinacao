from datetime import date

class Vacinacao():
  def __init__(self, codigo_vacinacao: int, data_vacinacao: date, data_retorno: date):
    if isinstance(codigo_vacinacao, int):
      self.__codigo_vacinacao = codigo_vacinacao
    if isinstance (data_vacinacao, date):
      self.__data_vacinacao = data_vacinacao
    if isinstance (data_retorno, date):
      self.__data_retorno = date

  @property
  def codigo_vacinacao(self):
    return self.__codigo_vacinacao
    
  @codigo_vacinacao.setter
  def codigo_vacinacao (self, codigo_vacinacao: int):
    if isinstance(codigo_vacinacao, int):
      self.__codigo_vacinacao = codigo_vacinacao

  @property
  def data_vacinacao(self):
    return self.__data_vacinacao
  
  @data_vacinacao.setter
  def data_vacinacao (self, data_vacinacao: date):
    if isinstance (data_vacinacao, date):
      self.__data_vacinacao = data_vacinacao

  @property
  def data_retorno(self):
    return self.__data_retorno
  
  @data_retorno.setter
  def data_retorno (self, data_retorno: date):
    if isinstance (data_retorno, date):
      self.__data_vacinacao = data_retorno