import Pessoa
from datetime import date

class Paciente(Pessoa):

  def __init__(self, nome: str, cpf: int, data_de_nascimento: date, telefone: int,       nome_responsavel: str, idade: int):
    super().__init__(nome, cpf, data_de_nascimento, telefone) 
    if isinstance (nome_responsavel, str):
      self.__nome_responsavel = nome_responsavel
    if isinstance (idade, int):
      self.__idade = idade

  @property
  def nome_responsavel(self):
    return self.__nome_responsavel

  @nome_responsavel.setter
  def nome_responvabel(self, nome_responsavel: str):
    if isinstance(nome_responsavel, str):
      self.__nome_responsabel = nome_responsavel

  @property
  def idade(self):
    return self.__idade 

  @idade.setter
  def idade(self, idade: int):
    if isinstance (idade, int):
      self.__idade = idade

    
  
