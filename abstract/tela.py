from abc import ABC
from errors.BadInputValue import BadInputValue

from errors.IsEmptyError import IsEmptyError


class Tela:
  def __init__(self, titulo, objeto, opcoes):
    ''' titulo: str '''
    self.__titulo = titulo
    '''
    objeto: [key: str]: [Nome: str, tipo: <T>, editavel: bool, f_validar(), *args]
    '''
    self.__objeto = objeto
    ''' opcoes: [key: int]: [Descricao: str, funcao()] '''
    self.__opcoes = opcoes

  @property
  def titulo(self):
    return self.__titulo

  @property
  def objeto(self):
    return self.__objeto
  
  @property
  def opcoes(self):
    return self.__opcoes

  def inserir_inteiro(self, message, opcoes: list = None) -> int:
    if opcoes: print(f"Insira um valor numérico inteiro dentre as seguintes opções: {' '.join([str(x) for x in opcoes])}")
    while True:
      try:
        i = int(input(message))
        if opcoes:
          if i not in opcoes:
            raise ValueError

      except ValueError:
        if not opcoes: 
          print('Insira um valor numérico inteiro.')
        elif opcoes: 
          print(f"Insira um valor numérico inteiro dentre as seguintes opções: {' '.join([str(x) for x in opcoes])}")
      else:
        return int(i)
    
  def inserir_string(self, mensagem = 'Insira uma string', min_len = None, max_len = None):
    texto = '\n'+mensagem
    print(texto)
    while True:
      try:
        entrada = input('Entrada: ')
        if entrada.strip() == '':
          raise IsEmptyError
        if min_len and len(entrada) < min_len:
          raise BadInputValue
        if max_len and len(entrada) > max_len:
          raise BadInputValue
      
      except (BadInputValue, IsEmptyError) as e:
        print(e)
        texto = '\n'+mensagem    
        if min_len: texto += f'\n- No mínimo {min_len} caracteres'
        if max_len: texto += f'\n- No máximo {max_len} caracteres'
        print(texto)
      else:
        return entrada

  def inserir_enum(self, mensagem, opcoes: dict):
    for opcao, tipo in opcoes.items():
      print(f'{opcao} - {tipo}')
    entrada = self.inserir_inteiro(mensagem, opcoes)
    return opcoes[entrada]

  def mostrar_opcoes(self):
    escolha = 0
    print(f'\n--- {self.titulo} ---')
    for opcao, data in self.opcoes.items():
      print(f'{opcao} - {data[0]}')
    escolha = self.inserir_inteiro('\nDigite a opção escolhida: ', list(self.opcoes.keys()))
    
    self.opcoes[escolha][1]()

  def pegar_dados(self) -> dict:
    objeto = {}
    for atributo, data in self.objeto.items():
      if(data[2]):
        if(data[4]):
          # se houver params, chama a função com os parâmetros
          valor = data[3](*data[4])
        else:
          valor = data[3]()
        objeto[atributo] = valor
    
    return objeto
