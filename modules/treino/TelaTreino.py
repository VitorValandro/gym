from abstract.tela import Tela
from errors import IsEmptyError, NotFound
from errors.MandatoryRelationshipIsEmpty import MandatoryRelationshipIsEmpty

class TelaTreino(Tela):
  def __init__(self, controlador, tela_aluno, tela_exercicio):
    titulo = 'Treino'
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome: ']],
      "aluno": ['Aluno', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do aluno: ', tela_aluno, 'Alunos']],
    }
    opcoes = {
      1: ['Cadastrar um treino', self.cadastrar],
      2: ['Editar um treino', self.editar],
      3: ['Listar treinos', self.listar],
      4: ['Deletar um treino', self.deletar],
      5: ['Voltar', self.voltar]
    }

    self.objeto_pratica = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "repeticoes": ['Repeticoes', str, True, self.inserir_inteiro, ['Insira o numero de repeticoes: ']],
      "peso": ['Peso', str, True, self.inserir_float, ['Insira o peso: ']],
      "exercicio": ['Exercicio', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do exercicio: ', tela_exercicio, 'Exercicios']],
    }
    super().__init__(titulo, objeto, opcoes, controlador)

  def cadastrar(self):
    try:
      dados = self.pegar_dados()
      praticas = self.cadastrar_praticas()
    except MandatoryRelationshipIsEmpty as e:
      print(e)
      return
    try:
      self.controlador.cadastrar(dados, praticas)
    except:
      print(f'Ocorreu um problema ao cadastrar o treino. Tente novamente.')
      raise
    else:
      print('Treino cadastrado com sucesso.')

  def editar(self):
    try:
      id_registros = self.listar()
      identificador = self.inserir_inteiro('Digite o id que deseja editar: ', id_registros)
      dados = self.pegar_dados()

      opcao = self.opcoes_edicao_pratica()
      if opcao == 1:
        dados_praticas_cadastro = self.cadastrar_praticas()
        self.controlador.cadastrar_pratica(identificador, dados_praticas_cadastro)
      if opcao == 2:
        dados_praticas_edicao = self.editar_praticas(identificador)
        self.controlador.editar(identificador, dados, dados_praticas_edicao)
      if opcao == 3:
        self.listar_praticas(identificador)
      if opcao == 4:
        self.deletar_pratica(identificador)
      if opcao == 5:
        self.controlador.editar(identificador, dados, [])
    
    except IsEmptyError:
      print(f'N??o h?? {self.titulo} cadastrados ainda.')
    except NotFound:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
    except:
      print(f'Ocorreu um problema ao editar o objeto. Tente novamente.')
    else:
      print(f'Treino editado com sucesso.')

  def opcoes_edicao_pratica(self):
    print()
    print('1 - Cadastrar um novo pr??tica')
    print('2 - Editar um pr??tica existente')
    print('3 - Listar pr??ticas do treino')
    print('4 - Deletar um pr??tica')
    print('5 - N??o quero editar as pr??ticas')
    return self.inserir_inteiro('Escolha a op????o: ', [1,2,3,4,5])

  def cadastrar_praticas(self):
    print("\n-- Cadastrar pr??ticas do treino --\n")
    praticas = []
    registrar_praticas = ''
    while registrar_praticas.lower() != 'n':
      dados_pratica = self.pegar_dados(self.objeto_pratica)
      praticas.append(dados_pratica)

      registrar_praticas = self.inserir_string("Continuar cadastrando pr??ticas? (digite 'n' para parar)")
      
    return praticas

  def editar_praticas(self, id_treino):
    print("\n-- Editar pr??ticas do treino --\n")
    praticas_editados = []
    editando_praticas = ''
    while editando_praticas.lower() != 'n':
      id_praticas = self.listar_praticas(id_treino)
      identificador_pratica = self.inserir_inteiro('Digite o id que deseja editar: ', id_praticas)
      dados_pratica = self.pegar_dados(self.objeto_pratica)
      dados_pratica['id'] = identificador_pratica
      dados_pratica['treino'] = id_treino
      praticas_editados.append(dados_pratica)

      editando_praticas = self.inserir_string("Continuar editando pr??ticas? (digite 'n' para parar)")
    
    return praticas_editados

  def visualizar_praticas(self, id_treino):
    [treino, _] = self.controlador.buscar_por_id(id_treino)
    print('Pr??ticas:')
    for pratica in treino.praticas:
      print(f"\t{'-'*10}")
      print(f'\tRepeti????es: {pratica["repeticoes"]}')
      print(f'\tPeso: {pratica["peso"]}')
      print(f'\tExerc??cio: {pratica["exercicio"]}')

  def listar_praticas(self, id_treino):
    [treino, _] = self.controlador.buscar_por_id(id_treino)
    id_praticas = []
    print(f'\n-- Lista de Pr??ticas --')
    for pratica in treino.praticas:
      id_praticas.append(pratica["id"])
      print()
      print(f'ID: {pratica["id"]}')
      print(f'Repeti????es: {pratica["repeticoes"]}')
      print(f'Peso: {pratica["peso"]}')
      print(f'Exerc??cio: {pratica["exercicio"]}')
    
    return id_praticas

  def deletar_pratica(self, id_treino):
    try:
      id_registros = self.listar_praticas(id_treino)
      identificador = self.inserir_inteiro('Digite o id que deseja deletar: ', id_registros)
      self.controlador.deletar_pratica(identificador)
    except IsEmptyError:
      print(f'N??o h?? pr??ticas cadastradas ainda.')
      return
    except NotFound:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
      return
    except:
      print(f'Ocorreu um problema ao deletar o objeto. Tente novamente.')
      return
    else:
      print(f'Pr??tica deletada com sucesso.')
