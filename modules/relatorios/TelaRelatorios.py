from abstract.tela import Tela
from errors.IsEmptyError import IsEmptyError
from errors.MandatoryRelationshipIsEmpty import MandatoryRelationshipIsEmpty

class TelaRelatorios(Tela):
  def __init__(self, controlador, tela_aluno, tela_professor):
    titulo = 'Relatórios'
    objeto = None
    opcoes = {
      1: ['Totalização dos treinos de um aluno por avaliação', self.avaliacao_treinos_por_aluno],
      2: ['Avaliações de treino de um determinado professor', self.avaliacao_treinos_por_professor],
      3: ['Exercícios de acordo com a sua função/agrupamento', self.exercicios_por_agrupamento],
      4: ['Totalização do gasto com professores', self.totalizacao_gasto_professores],
      5: ['Aparelhos de acordo com sua quantidade e número de exercícios em que é utilizado', 
            self.aparelho_por_quantidade_e_exercicios],
      6: ['Média de tempo para cada tipo de treino de um aluno', self.media_tempo_por_treino_aluno],
      7: ['Voltar', self.voltar]
    }
    super().__init__(titulo, objeto, opcoes, controlador)
    self.tela_aluno = tela_aluno
    self.tela_professor = tela_professor

  def avaliacao_treinos_por_aluno(self):
    try:
      id_aluno = self.selecionar_estrangeiro('Selecione um aluno: ', self.tela_aluno, 'Alunos')
    except MandatoryRelationshipIsEmpty as e:
      print(e)
      return
    try:
      resultados = self.controlador.avaliacao_treinos_por_aluno(id_aluno)
      print()
      for resultado in resultados:
        print('-'*20)
        print(f"Avaliação: {resultado['avaliacao']}")
        print(f"Número de treinos: {resultado['numero_treinos']}")
    except IsEmptyError:
      print('Dados insuficientes para gerar este relatório. Cadastre treinos e tente novamente.')

  def avaliacao_treinos_por_professor(self):
    try:
      id_professor = self.selecionar_estrangeiro('Selecione um professor: ', self.tela_professor, 'Professores')
    except MandatoryRelationshipIsEmpty as e:
      print(e)
      return
    try:
      resultados = self.controlador.avaliacao_treinos_por_professor(id_professor)
      print()
      for resultado in resultados:
        print('-'*20)
        print(f"Avaliação: {resultado['avaliacao']}")
        print(f"Número de treinos: {resultado['numero_treinos']}")
    except IsEmptyError:
      print('Dados insuficientes para gerar este relatório. Cadastre treinos e tente novamente.')

  def exercicios_por_agrupamento(self):
    try:
      resultados = self.controlador.exercicios_por_agrupamento()
      print()
      for resultado in resultados:
        print('-'*20)
        print(f"Tipo: {resultado['tipo']}")
        print(f"Número de exercícios: {resultado['numero_exercicios']}")
    except IsEmptyError:
      print('Dados insuficientes para gerar este relatório. Cadastre exercícios e tente novamente.')

  def totalizacao_gasto_professores(self):
    try:
      resultados = self.controlador.totalizacao_gasto_professores()
      print()
      for resultado in resultados:
        print('-'*20)
        print(f"Número de professores: {resultado['numero_professores']}")
        print(f"Total gasto em salário: {resultado['total_salario']}")
        print(f"Média salarial: {float(resultado['media_salario']):.2f}")
    except IsEmptyError:
      print('Dados insuficientes para gerar este relatório. Cadastre professores e tente novamente.')

  def aparelho_por_quantidade_e_exercicios(self):
    try:
      resultados = self.controlador.aparelho_por_quantidade_e_exercicios()
      print()
      for resultado in resultados:
        print('-'*60)
        print(f"Nome do aparelho: {resultado['nome']}")
        print(f"Número de aparelhos que a academia possui: {resultado['quantidade']}")
        print(f"Número de exerícios em que o aparelho é utilizado: {resultado['numero_exercicios']}")
    except IsEmptyError:
      print('Dados insuficientes para gerar este relatório. Cadastre aparelhos e exercícios e tente novamente.')

  def media_tempo_por_treino_aluno(self):
    try:
      id_aluno = self.selecionar_estrangeiro('Selecione um aluno: ', self.tela_aluno, 'Alunos')
    except MandatoryRelationshipIsEmpty as e:
      print(e)
      return
    try:
      resultados = self.controlador.media_tempo_por_treino_aluno(id_aluno)
      print()
      for resultado in resultados:
        print('-'*45)
        print(f"Treino realizado: {resultado['nome_treino']}")
        print(f"Média de tempo gasto: {float(resultado['media_tempo']):.2f} minutos")
        print(f"Número de treinos realizados: {resultado['numero_treinos']}")
    except IsEmptyError:
      print('Dados insuficientes para gerar este relatório. Cadastre treinos e tente novamente.')