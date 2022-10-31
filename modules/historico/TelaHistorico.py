from abstract.tela import Tela

class TelaHistorico(Tela):
  def __init__(self, controlador, tela_aluno, tela_professor, tela_treino):
    titulo = 'Histórico'
    avaliacoes = {
      1: 'BOM',
      2: 'MÉDIO',
      3: 'RUIM'
    }
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "data": ['Data de realização', int, False, None, None],
      "tempo": ['Tempo', int, True, self.inserir_inteiro, ['Insira o tempo do treino (em minutos): ']],
      "avaliacao": ['Avaliação', str, True, self.inserir_enum, ['Avalie o treino: ', avaliacoes]],
      "aluno": ['Aluno', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do aluno: ', tela_aluno, 'Alunos']],
      "professor": ['Professor', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do professor: ', tela_professor, 'Professores']],
      "treino": ['Treino', int, True, self.selecionar_estrangeiro, 
        ['Selecione o id do treino: ', tela_treino, 'Treinos']],
    }
    opcoes = {
      1: ['Cadastrar um histórico', self.cadastrar],
      2: ['Listar históricos', self.listar],
      3: ['Voltar', self.voltar]
    }
    super().__init__(titulo, objeto, opcoes, controlador)