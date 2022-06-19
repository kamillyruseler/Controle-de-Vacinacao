

class Vacina():
  def __init__(self, doenca, faixa_etaria_inicial: int, faixa_etaria_final: int):
    if isinstance (doenca, str):
      self.__doenca = doenca
    if isinstance (faixa_etaria_inicial, int):
      self.__faixa_etaria_inicial = faixa_etaria_inicial
    if isinstance (faixa_etaria_final, int):
      self.__faixa_etaria_final = faixa_etaria_final

  @property
  def doenca(self):
    return self.__doenca

  @doenca.setter
  def doenca (self, doenca: str):
    if isinstance (doenca, str):
      self.__doenca = doenca

  @property
  def faixa_etaria_inicial (self):
    return self.__faixa_etaria_inicial

  @faixa_etaria_inicial.setter
  def faixa_etaria_inicial (self, faixa_etaria_inicial: int):
    if isinstance (faixa_etaria_inicial, int):
      self.__faixa_etaria_inicial = faixa_etaria_inicial

  @property
  def faixa_etaria_final (self):
    return self.__faixa_etaria_final

  @faixa_etaria_final.setter
  def faixa_etaria_final (self, faixa_etaria_final: int):
    if isinstance (faixa_etaria_final, int):
      self.__faixa_etaria_final = faixa_etaria_final