import random
from modules.aparelho.AparelhoDAO import AparelhoDAO


class Aparelho(AparelhoDAO):

    def __init__(self, nome: str, quantidade: int, tipo: str, id=None) -> None:
        if not id:
            id = random.randint(1000, 9999)
        super().__init__()
        self.__id = id
        self.__nome = nome
        self.__quantidade = quantidade
        self.__tipo = tipo

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
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @staticmethod
    def buscar() -> list:
        return AparelhoDAO.buscar()
