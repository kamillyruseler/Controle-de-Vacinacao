

class Dose():
  def __init__(self, doenca: str, lote: str):
    if isinstance(doenca, str):
      self.__doenca = doenca
    if isinstance(lote, str):
      self.__lote = lote

      
  @property
  def lote(self):
    return self.__lote

  @lote.setter
  def lote(self, lote: str):
    if isinstance(lote, str):
      self.__lote = lote

  @property
  def doenca(self):
    return self.__doenca

  @doenca.setter
  def doenca(self, doenca: str):
    if isinstance(doenca, str):
      self.__doenca = doenca

      