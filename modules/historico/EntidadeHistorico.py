import random
from modules.pessoa.aluno.EntidadeAluno import Aluno
from modules.pessoa.professor.EntidadeProfessor import Professor
from modules.treino.EntidadeTreino import Treino
from modules.historico.HistoricoDAO import HistoricoDAO


class Historico(HistoricoDAO):

    def __init__(
        self,
        data: str,
        tempo: int,
        avaliacao: str,
        aluno: Aluno,
        professor: Professor,
        treino: Treino,
        id=None
    ) -> None:
        super().__init__()
        if not id:
            id = random.randint(1000, 9999)
        self.__id = id
        self.__data = data
        self.__tempo = tempo
        self.__avaliacao = avaliacao
        self.__aluno = aluno
        self.__professor = professor
        self.__treino = treino

    @property
    def identificador(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def tempo(self):
        return self.__tempo

    @tempo.setter
    def tempo(self, tempo):
        self.__tempo = tempo

    @property
    def avaliacao(self):
        return self.__avaliacao

    @avaliacao.setter
    def avaliacao(self, avaliacao):
        self.__avaliacao = avaliacao

    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    @property
    def treino(self):
        return self.__treino

    @treino.setter
    def treino(self, treino):
        self.__treino = treino

    @staticmethod
    def buscar() -> list:
        return HistoricoDAO.buscar()
