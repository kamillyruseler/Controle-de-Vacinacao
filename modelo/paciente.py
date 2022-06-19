from modelo.pessoa import Pessoa
from datetime import date

class Paciente(Pessoa):

  def __init__(self, nome: str, cpf: int, data_de_nascimento: date, telefone: int,       nome_responsavel: str):
    super().__init__(nome, cpf, data_de_nascimento, telefone) 
    if isinstance (nome_responsavel, str):
      self.__nome_responsavel = nome_responsavel
    

  @property
  def nome_responsavel(self):
    return self.__nome_responsavel

  @nome_responsavel.setter
  def nome_responsavel(self, nome_responsavel: str):
    if isinstance(nome_responsavel, str):
      self.__nome_responsabel = nome_responsavel



    
  
