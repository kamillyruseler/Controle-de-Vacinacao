from modelo.pessoa import Pessoa
from datetime import date

class Enfermeiro (Pessoa):
  def __init__(self, nome: str, cpf: int, data_de_nascimento: date, telefone, email, senha:str, codigo_enfermeiro):
    super().__init__(nome, cpf, data_de_nascimento, telefone)
    if isinstance (email, str):
      self.__email = email
    if isinstance (senha, str):
      self.__senha = senha
    if isinstance (codigo_enfermeiro, int):
      self.__codigo_enfermeiro = codigo_enfermeiro

  @property
  def email (self):
    return self.__email

  @email.setter
  def email (self, email: str):
    if isinstance(email, str):
      self.__email = email

  @property
  def senha (self):
    return self.__senha 

  @senha.setter
  def senha (self, senha: str):
    if isinstance (senha, str):
      self.__senha = senha

  @property
  def codigo_enfermeiro(self) -> int:
    return self.__codigo_enfermeiro

  @codigo_enfermeiro.setter
  def codigo_enfermeiro (self, codigo_enfermeiro: int):
    if isinstance (codigo_enfermeiro, int):
      self.__codigo_enfermeiro = codigo_enfermeiro
