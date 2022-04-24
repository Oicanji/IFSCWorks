# Utilizacao a partir de listas
# vetor = [10, 11, 12]
# print(vetor)
# print(vetor[2])

# Usando a classe array do Python
# from array import array

# vetor2 = array('i', [10, 11, 12])
# print(vetor2)
# print(vetor2[2])

#usando NumPy
import numpy as np

# vector3 = np.array([10, 11, 12])
# print(vector3)
# print(vector3[2])

#class VetorNaoOrdenado
class VetorNaoOrdenado:

    def __init__(self, max):
        self.__ultima_posicao = 0
        self.__vetor = np.zeros(max)
        self.maxima_capacidade = max

    def getMax(self):
        return self.maxima_capacidade

    def thisEmpty(self):
        if(self.maxima_capacidade == self.__ultima_posicao):
            return True
        return False

    def addVetor(self, valor):
        if not self.thisEmpty():
            self.__vetor[self.__ultima_posicao] = valor
            self.__ultima_posicao+=1
            return True
        return "Vetor cheio"
    

    def printEmpty(self):
        if self.thisEmpty():
            return "Vetor cheio"
        return "Vetor livre"

    def returnVetor(self):
        return_list = []
        i = 0
        while( i <= self.__ultima_posicao-1  ):
            return_list.append(str(self.__vetor[i]))
            i+=1
        return return_list

vetor_classe = VetorNaoOrdenado(10)
vetor_classe.addVetor(12)
vetor_classe.addVetor(22)
vetor_classe.addVetor(31)
vetor_classe.addVetor(72)

resultados_print = vetor_classe.returnVetor()
for text in resultados_print:
    print(" [",text,"] ")
