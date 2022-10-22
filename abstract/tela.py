from abc import ABC
from errors import NotFound
from errors.BadInputValue import BadInputValue
from errors.IsEmptyError import IsEmptyError


class Tela:
  def __init__(self, titulo, objeto, opcoes, controlador):
    ''' titulo: str '''
    self.__titulo = titulo
    '''
    objeto: [key: str]: [Nome: str, tipo: <T>, editavel: bool, f_validar(), *args]
    '''
    self.__objeto = objeto
    ''' opcoes: [key: int]: [Descricao: str, funcao()] '''
    self.__opcoes = opcoes
    ''' controlador: classe de controlador'''
    self.__controlador = controlador

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
  
  def inserir_float(self, message, opcoes: list = None) -> int:
    if opcoes: print(f"Insira um valor numérico decimal dentre as seguintes opções: {' '.join([str(x) for x in opcoes])}")
    while True:
      try:
        i = float(input(message))
        if opcoes:
          if i not in opcoes:
            raise ValueError

      except ValueError:
        if not opcoes: 
          print('Insira um valor numérico valido.')
        elif opcoes: 
          print(f"Insira um valor numérico dentre as seguintes opções: {' '.join([str(x) for x in opcoes])}")
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

  def selecionar_estrangeiro(self, mensagem, controlador_estrangeiro, entidade_estrangeira):
    try:
      id_estrangeiros = self.listar(controlador_estrangeiro, entidade_estrangeira)
      chave_estrangeira = self.inserir_inteiro(mensagem, id_estrangeiros)
    except IsEmptyError:
      print(f'Não há {entidade_estrangeira} cadastrados ainda. Faça o cadastro de {entidade_estrangeira} antes de prosseguir.')
      return
    return chave_estrangeira
      
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
      if(data[2]): # se for editável
        if(data[4]): # se houver params, chama a função com os parâmetros
          valor = data[3](*data[4])
        else:
          valor = data[3]()
        objeto[atributo] = valor
    
    return objeto

  def cadastrar(self):
    dados = self.pegar_dados()
    try:
      self.__controlador.cadastrar(dados)
    except:
      print(f'Ocorreu um problema ao cadastrar o objeto. Tente novamente.')
      raise
    else:
      print('Objeto cadastrado com sucesso.')

  def editar(self):
    try:
      id_registros = self.listar()
      identificador = self.inserir_inteiro('Digite o id que deseja editar: ', id_registros)
      dados = self.pegar_dados()
      self.__controlador.editar(identificador, dados)
    except IsEmptyError:
      print(f'Não há {self.titulo} cadastrados ainda.')
    except NotFound:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
    except:
      print(f'Ocorreu um problema ao editar o objeto. Tente novamente.')
    else:
      print(f'Editado com sucesso.')
  
  def listar(self, colecao = 1, titulo = 1) -> list:
    if colecao == 1: colecao = self.__controlador.colecao
    if titulo == 1: titulo = self.titulo
    identificadores = []
    if len(colecao):
      print(f'\n-- Lista de {titulo} --')
      for objeto in colecao:
        identificadores.append(objeto.identificador)
        print(f'{objeto.identificador} - {objeto.nome}')
      print()
      return identificadores
    else:
      raise IsEmptyError
  
  def deletar(self):
    try:
      id_registros = self.listar()
      identificador = self.inserir_inteiro('Digite o id que deseja deletar: ', id_registros)
      self.__controlador.deletar(identificador)
    except IsEmptyError:
      print(f'Não há {self.titulo} cadastrados ainda.')
      return
    except NotFound:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
      return
    except:
      print(f'Ocorreu um problema ao deletar o objeto. Tente novamente.')
      return
    else:
      print(f'Deletado com sucesso.')
