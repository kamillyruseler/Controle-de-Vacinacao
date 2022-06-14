from controle.controlador_enfermeiro import ControladorEnfermeiro
from visao.tela_sistema import TelaSistema


class ControladorSistema:
  def __init__(self):
      self.__controlador_enfermeiro = ControladorEnfermeiro()
      self.__tela_sistema = TelaSistema()

  def iniciar(self):
      while True:
          opcao_escolhida = self.__tela_sistema.mostrar_menu_inicial()
          if opcao_escolhida == 1:
            if (self.__controlador_enfermeiro.logar()):
              self.__controlador_enfermeiro.abre_tela_inicial()
            elif opcao_escolhida == 2:
              pass
            else:
              break

if __name__ == "__main__":
    ControladorSistema().iniciar()

    
    