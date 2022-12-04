import random
from modules.exercicio.EntidadeExercicio import Exercicio
from modules.treino.EntidadeTreino import Treino
from modules.treino.pratica.PraticaDAO import PraticaDAO


class Pratica(PraticaDAO):

    def __init__(self, repeticoes: int, peso: float, exercicio: Exercicio, treino: Treino, id=None) -> None:
        if not id:
            id = random.randint(1000, 9999)
        super().__init__()
        self.__id = id
        self.__repeticoes = repeticoes
        self.__peso = peso
        self.__exercicio = exercicio
        self.__treino = treino

    @property
    def identificador(self):
        return self.__id

    @property
    def repeticoes(self):
        return self.__repeticoes

    @repeticoes.setter
    def repeticoes(self, repeticoes):
        self.__repeticoes = repeticoes

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def exercicio(self):
        return self.__exercicio

    @exercicio.setter
    def exercicio(self, exercicio):
        self.__exercicio = exercicio

    @property
    def treino(self):
        return self.__treino

    @treino.setter
    def treino(self, treino):
        self.__treino = treino

    @staticmethod
    def buscar() -> list:
        return PraticaDAO.buscar()
