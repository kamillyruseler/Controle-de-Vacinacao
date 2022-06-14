from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):

  @abstractmethod
  def __init__(self, nome: str, cpf: int, data_de_nascimento: date, telefone:int):
    if isinstance(nome, str):
      self.__nome = nome
    if isinstance (cpf, int):
      self.__cpf = cpf
    if isinstance (data_de_nascimento, date):
      self.__data_de_nascimento = data_de_nascimento
    if isinstance (telefone, int):
      self.__telefone = telefone

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    if isinstance(nome, str):
      self.__nome = nome

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf (self, cpf: int):
    if isinstance(cpf, int):
      self.__cpf = cpf

  @property
  def data_de_nascimento (self):
    return self.__data_de_nascimento

  @data_de_nascimento.setter
  def data_de_nascimento (self, data_de_nascimento: date):
    if isinstance (data_de_nascimento, date):
      self.__data_de_nascimento = data_de_nascimento

  @property
  def telefone (self):
    return self.__telefone

  @telefone.setter
  def telefone (self, telefone: int):
    if isinstance (telefone, int):
      self.__telefone = telefone
