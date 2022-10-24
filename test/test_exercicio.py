import sqlite3
import unittest
from modules.aparelho.ControladorAparelho import ControladorAparelho

from modules.exercicio.ControladorExercicio import ControladorExercicio

class TestExercicio(unittest.TestCase):
  connection = sqlite3.connect('test.db')
  connection.row_factory = sqlite3.Row 
  cursor = connection.cursor()
  controlador_mock = ControladorExercicio()
  controlador_aparelhos_mock = ControladorAparelho()

  def cadastrar(self):
    dados_aparelho_mock = {
      "id": 1111,
      "nome": 'teste',
      "quantidade": 1,
      "tipo": "HACK"
    }
    self.controlador_aparelhos_mock.cadastrar(dados_aparelho_mock)
    dados_mock = {
      "id": 0000,
      "nome": 'teste',
      "aparelho": 1111,
      "tipo": "BRAÇOS"
    }
    self.controlador_mock.cadastrar(dados_mock)
    res = self.cursor.execute(f"SELECT nome FROM Exercicio WHERE id = {dados_mock['id']}")
    result = dict(res.fetchone())
    return (dados_mock['nome'], result['nome'])
  
  def editar(self):
    dados_mock = {
      "id": 0000,
      "nome": 'teste 2',
      "aparelho": 1111,
      "tipo": "PERNAS"
    }
    self.controlador_mock.editar(dados_mock['id'], dados_mock)
    res = self.cursor.execute(f"SELECT * FROM Exercicio WHERE id = {dados_mock['id']}")
    result = res.fetchone()
    return (dados_mock, dict(result))
  
  def deletar(self):
    dados_mock = { "id": 0000 }
    self.controlador_mock.deletar(dados_mock['id'])
    res = self.cursor.execute(f"SELECT * FROM Exercicio WHERE id = {dados_mock['id']}")
    result = res.fetchone()

    self.controlador_aparelhos_mock.deletar(1111)
    return (None, result)
  
  def test(self):
    self.assertEqual(*self.cadastrar())
    self.assertEqual(*self.editar())
    self.assertEqual(*self.deletar())

if __name__ == '__main__':
  unittest.main()