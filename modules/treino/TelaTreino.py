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

  def listar(self,) -> list:
    identificadores = []
    if len(self.controlador.colecao):
      print(f'\n-- Lista de Treinos --')
      for item in self.controlador.colecao:
        print()
        identificadores.append(item.identificador)
        print(f'ID: {item.identificador}')
        for atributo in [atributo for atributo in item.atributos if not atributo == 'id']:
          print(f'{self.objeto[atributo][0]}: {getattr(item, atributo)}')
        self.visualizar_praticas(item.identificador)
      print()
      return identificadores
    else:
      print(f'Não há {self.titulo} cadastrados ainda.')
      return

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
      print(f'Não há {self.titulo} cadastrados ainda.')
    except NotFound:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
    except:
      print(f'Ocorreu um problema ao editar o objeto. Tente novamente.')
    else:
      print(f'Treino editado com sucesso.')

  def opcoes_edicao_pratica(self):
    print()
    print('1 - Cadastrar um novo prática')
    print('2 - Editar um prática existente')
    print('3 - Listar práticas do treino')
    print('4 - Deletar um prática')
    print('5 - Não quero editar as práticas')
    return self.inserir_inteiro('Escolha a opção: ', [1,2,3,4,5])

  def cadastrar_praticas(self):
    print("\n-- Cadastrar práticas do treino --\n")
    praticas = []
    registrar_praticas = ''
    while registrar_praticas.lower() != 'n':
      dados_pratica = self.pegar_dados(self.objeto_pratica)
      praticas.append(dados_pratica)

      registrar_praticas = self.inserir_string("Continuar cadastrando práticas? (digite 'n' para parar)")
      
    return praticas

  def editar_praticas(self, id_treino):
    print("\n-- Editar práticas do treino --\n")
    praticas_editados = []
    editando_praticas = ''
    while editando_praticas.lower() != 'n':
      id_praticas = self.listar_praticas(id_treino)
      identificador_pratica = self.inserir_inteiro('Digite o id que deseja editar: ', id_praticas)
      dados_pratica = self.pegar_dados(self.objeto_pratica)
      dados_pratica['id'] = identificador_pratica
      dados_pratica['treino'] = id_treino
      praticas_editados.append(dados_pratica)

      editando_praticas = self.inserir_string("Continuar editando práticas? (digite 'n' para parar)")
    
    return praticas_editados

  def visualizar_praticas(self, id_treino):
    [treino, _] = self.controlador.buscar_por_id(id_treino)
    print('Práticas:')
    for pratica in treino.praticas:
      print(f"\t{'-'*10}")
      print(f'\tRepetições: {pratica["repeticoes"]}')
      print(f'\tPeso: {pratica["peso"]}')
      print(f'\tExercício: {pratica["exercicio"]}')

  def listar_praticas(self, id_treino):
    [treino, _] = self.controlador.buscar_por_id(id_treino)
    id_praticas = []
    print(f'\n-- Lista de Práticas --')
    for pratica in treino.praticas:
      id_praticas.append(pratica["id"])
      print()
      print(f'ID: {pratica["id"]}')
      print(f'Repetições: {pratica["repeticoes"]}')
      print(f'Peso: {pratica["peso"]}')
      print(f'Exercício: {pratica["exercicio"]}')
    
    return id_praticas

  def deletar_pratica(self, id_treino):
    try:
      id_registros = self.listar_praticas(id_treino)
      identificador = self.inserir_inteiro('Digite o id que deseja deletar: ', id_registros)
      self.controlador.deletar_pratica(identificador)
    except IsEmptyError:
      print(f'Não há práticas cadastradas ainda.')
      return
    except NotFound:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
      return
    except:
      print(f'Ocorreu um problema ao deletar o objeto. Tente novamente.')
      return
    else:
      print(f'Prática deletada com sucesso.')
