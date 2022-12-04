import random
from modules.pessoa.aluno.EntidadeAluno import Aluno
from modules.treino.TreinoDAO import TreinoDAO


class Treino(TreinoDAO):

    def __init__(self, nome: str, aluno: Aluno, id=None) -> None:
        if not id:
            id = random.randint(1000, 9999)
        super().__init__()
        self.__id = id
        self.__nome = nome
        self.__aluno = aluno
        self.__praticas_ = None

    @property
    def identificador(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno

    @property
    def praticas(self):
        return self.__praticas_

    @praticas.setter
    def praticas(self, praticas: list):
        self.__praticas_ = praticas

    @staticmethod
    def buscar() -> list:
        return TreinoDAO.buscar()
