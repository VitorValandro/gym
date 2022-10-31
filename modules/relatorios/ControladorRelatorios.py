import sqlite3

from errors.IsEmptyError import IsEmptyError

class ControladorRelatorios:
  def __init__(self):
    self.connection = sqlite3.connect('test.db')
    self.connection.row_factory = sqlite3.Row   
    self.cursor = self.connection.cursor()

  def avaliacao_treinos_por_aluno(self, id_aluno):
    try:
      res = self.cursor.execute(f'''
        SELECT 
          Historico.avaliacao,
          COUNT(Historico.id) as numero_treinos,
          Aluno.nome as aluno
        FROM 
          Historico
          INNER JOIN Aluno ON Aluno.id = Historico.aluno
        WHERE
          Historico.aluno = {id_aluno}
        GROUP BY Historico.avaliacao
      ''')
      resultado = [dict(row) for row in res.fetchall()]
      if not len(resultado):
        raise IsEmptyError
      return resultado
    except:
      raise IsEmptyError

  def avaliacao_treinos_por_professor(self, id_professor):
    try:
      res = self.cursor.execute(f'''
        SELECT 
          Historico.avaliacao,
          COUNT(Historico.id) as numero_treinos,
          Professor.nome as professor
        FROM 
          Historico
          INNER JOIN Professor ON Professor.id = Historico.professor
        WHERE
          Historico.professor = {id_professor}
        GROUP BY Historico.avaliacao
      ''')
      resultado = [dict(row) for row in res.fetchall()]
      if not len(resultado):
        raise IsEmptyError
      return resultado
    except:
      raise IsEmptyError
  
  def exercicios_por_agrupamento(self):
    try:
      res = self.cursor.execute(f'''
        SELECT 
          tipo,
          COUNT(id) as numero_exercicios
        FROM
          Exercicio
        GROUP BY
          Exercicio.tipo
      ''')
      resultado = [dict(row) for row in res.fetchall()]
      if not len(resultado):
        raise IsEmptyError
      return resultado
    except:
      raise IsEmptyError

  def totalizacao_gasto_professores(self):
    try:
      res = self.cursor.execute(f'''
        SELECT 
          COUNT(id) as numero_professores,
          SUM(salario) as total_salario,
          AVG(salario) as media_salario
        FROM
          Professor
      ''')
      resultado = [dict(row) for row in res.fetchall()]
      if not len(resultado):
        raise IsEmptyError
      return resultado
    except:
      raise IsEmptyError
  
  def aparelho_por_quantidade_e_exercicios(self):
    try:
      res = self.cursor.execute(f'''
        SELECT 
          Aparelho.nome,
          Aparelho.quantidade,
          COUNT(Aparelho.id) as numero_exercicios
        FROM
          Aparelho
          INNER JOIN Exercicio ON Exercicio.aparelho = Aparelho.id
        GROUP BY
          Exercicio.aparelho
      ''')
      resultado = [dict(row) for row in res.fetchall()]
      if not len(resultado):
        raise IsEmptyError
      return resultado
    except:
      raise IsEmptyError
  
  def media_tempo_por_treino_aluno(self, id_aluno):
    try:
      res = self.cursor.execute(f'''
        SELECT 
          AVG(Historico.tempo) as media_tempo,
          COUNT(Historico.id) as numero_treinos,
          Treino.nome as nome_treino,
          Aluno.nome as aluno
        FROM 
          Historico
          INNER JOIN Aluno ON Aluno.id = Historico.aluno
          INNER JOIN Treino ON Treino.id = Historico.treino
        WHERE
          Historico.aluno = {id_aluno}
        GROUP BY Historico.treino
      ''')
      resultado = [dict(row) for row in res.fetchall()]
      if not len(resultado):
        raise IsEmptyError
      return resultado
    except:
      raise IsEmptyError