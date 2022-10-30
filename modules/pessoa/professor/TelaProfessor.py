from abstract.tela import Tela
from errors import IsEmptyError, NotFound


class TelaProfessor(Tela):
  def __init__(self, controlador):
    titulo = 'Professores'
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome: ', 3, 15]],
      "cpf": ['CPF', str, True, self.inserir_string, ['Insira o CPF: ']],
      "peso": ['Peso', str, True, self.inserir_inteiro, ['Insira o peso: ']],
      "altura": ['Altura', str, True, self.inserir_float, ['Insira a altura: ']],
      "salario": ['Salário', str, True, self.inserir_float, ['Insira o salário: ']],
    }
    opcoes = {
      1: ['Cadastrar um professor', self.cadastrar],
      2: ['Editar um professor', self.editar],
      3: ['Listar professores', self.listar],
      4: ['Deletar um professor', self.deletar],
    }
    super().__init__(titulo, objeto, opcoes, controlador)
  
  def cadastrar(self):
    turnos = []
    dias_semana = {
      1: "Segunda Feira",
      2: "Terça Feira",
      3: "Quarta Feira",
      4: "Quinta Feira",
      5: "Sexta Feira",
      6: "Sábado"
    }
    periodos = {
      1: "Manhã",
      2: "Tarde",
      3: "Noite"
    }
    objeto_turno = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "dia_semana": ['Dia da semana', str, True, self.inserir_enum, ['Insira o dia da semana: ', dias_semana]],
      "periodo": ['Período', str, True, self.inserir_enum, ['Insira o período: ', periodos]],
      "carga_horaria": ['Carga horária', str, True, self.inserir_inteiro, ['Insira a carga horária: ']],
    }
    dados = self.pegar_dados()
    print("\n-- Cadastrar turnos do professor --\n")
    registrar_turnos = ''
    while registrar_turnos.lower() != 'n':
      dados_turno = self.pegar_dados(objeto_turno)
      registrar_turnos = self.inserir_string("Continuar cadastrando? (digite 'n' para parar)")
      turnos.append(dados_turno)
    try:
      self.controlador.cadastrar(dados, turnos)
    except:
      print(f'Ocorreu um problema ao cadastrar o professor. Tente novamente.')
      raise
    else:
      print('Professor cadastrado com sucesso.')
  
  def editar(self):
    ''' IMPLEMENTANDO '''
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