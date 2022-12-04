import random
from modules.exercicio.ExercicioDAO import ExercicioDAO


class Exercicio(ExercicioDAO):

    def __init__(self, nome: str, tipo: str, aparelho: int, id=None) -> None:
        if not id:
            id = random.randint(1000, 9999)
        super().__init__()
        self.__id = id
        self.__nome = nome
        self.__tipo = tipo
        self.__aparelho = aparelho

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
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def aparelho(self):
        return self.__aparelho

    @aparelho.setter
    def aparelho(self, aparelho):
        self.__aparelho = aparelho

    @staticmethod
    def buscar() -> list:
        return ExercicioDAO.buscar()
