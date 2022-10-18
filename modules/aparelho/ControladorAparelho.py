from modules.aparelho.EntidadeAparelho import Aparelho

class ControladorAparelho:
  def __init__(self):
    self.__aparelhos = []

  def cadastrar(self, dados: dict):
    novo_aparelho = Aparelho(**dados)
    novo_aparelho.guardar()
    self.__aparelhos.append(novo_aparelho)
  
  def atualizar(self, dados: dict):
    aparelho = Aparelho(**dados)
    aparelho.atualizar()

  def indice_por_id(self, id):
    # IMPLEMENTAR ISSO
    return self.__aparelhos.index(Aparelho(None, None, None, id))
    