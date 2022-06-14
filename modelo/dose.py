class Dose():
  def __init__(self, lote: str, codigo_aplicador: int, nome_aplicador: str):
    if isinstance(lote, str):
      self.__lote = lote
    if isinstance(codigo_aplicador, int):
      self.__codigo_aplicador = codigo_aplicador
    if isinstance(nome_aplicador, str):
      self.__nome_aplicador = nome_aplicador

  @property
  def lote(self):
    return self.__lote

  @lote.setter
  def lote(self, lote: str):
    if isinstance(lote, str):
      self.__lote = lote

  @property
  def codigo_aplicador(self):
    return self.__codigo_aplicador 

  @codigo_aplicador.setter
  def codigo_aplicador(self, codigo_aplicador: str):
    if isinstance (codigo_aplicador, int):
      self.__codigo_aplicador = codigo_aplicador

  @property
  def nome_aplicador(self):
    return self.__nome_aplicador

  @nome_aplicador.setter
  def nome_aplicador(self, nome_aplicador: str):
    if isinstance(nome_aplicador, str):
      self.__nome_responsavel = nome_aplicador



      