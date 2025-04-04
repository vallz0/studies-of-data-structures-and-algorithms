import numpy as np

class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numeros_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return ((self.inicio == 0 and self.final == self.capacidade - 1)
                or (self.inicio == self.final + 1))

    def __deque_vazio(self):
        return self.inicio == -1

    def insere_inicio(self,valor):
        if self.__deque_cheio():
            print('o deque esta cheio')
            return

        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        elif self.inicio == 0:
            self.inicio =  self.capacidade -1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor

    def insere_final(self,valor):
        if self.__deque_cheio():
            print('o deque esta cheio')
            return
        elif self.final ==self.capacidade - 1:
            self.final = 0
        else:
            self.final += 1

        self.valores[self.final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('o deque ja esta vazio')
            return

        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        else:
            if self.inicio == self.capacidade - 1:
                self.inicio = 0
            else:
                self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print('o deque ja esta vazio')
            return

        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        elif self.inicio == 0:
            self.final = self.capacidade - 1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio():
            print('o deque ja esta vazio')
            return
        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0:
            print('o deque ja esta vazio')
            return
        return self.valores[self.final]
