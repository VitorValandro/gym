from abstract.tela import Tela

class TelaHistorico(Tela):
  def __init__(self, controlador, controlador_aluno, controlador_professor, controlador_treino):
    titulo = 'Treino'
    avaliacoes = {
      1: 'BOM',
      2: 'MÉDIO',
      3: 'RUIM'
    }
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "tempo": ['Tempo', int, True, self.inserir_inteiro, ['Insira o tempo do treino (em minutos): ']],
      "avaliacao": ['Avaliação', str, True, self.inserir_enum, ['Avalie o treino: ', avaliacoes]],
      "aluno": ['Aluno', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do aluno: ', controlador_aluno.colecao, 'Alunos']],
      "professor": ['Professor', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do professor: ', controlador_professor.colecao, 'Professores']],
      "treino": ['Treino', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do treino: ', controlador_treino.colecao, 'Treinos']],
    }
    opcoes = {
      1: ['Cadastrar um histórico', self.cadastrar],
      2: ['Listar treinos', self.listar],
    }
    super().__init__(titulo, objeto, opcoes, controlador)

  def listar(self) -> list:
    identificadores = []
    if len(self.controlador.colecao):
      print(f'\n-- Lista de Históricos --')
      for historico in self.controlador.colecao:
        identificadores.append(historico.identificador)
        print()
        print(f'Aluno: {historico.aluno}')
        print(f'Professor: {historico.professor}')
        print(f'Treino: {historico.treino}')
        print(f'Avaliação: {historico.avaliacao}')
        print(f'Tempo: {historico.tempo} minutos')
        print(f'Data: {historico.data}')
      print()
      return identificadores
    else:
      print(f'Não há {self.titulo} cadastrados ainda.')
      return
