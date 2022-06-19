

class Dose():
  def __init__(self, lote: str):
    if isinstance(lote, str):
      self.__lote = lote

  @property
  def lote(self):
    return self.__lote

  @lote.setter
  def lote(self, lote: str):
    if isinstance(lote, str):
      self.__lote = lote


      