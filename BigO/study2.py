

def lista1() -> list[int]: # O(n)
    lista: list = []
    for i in range(1000):
        lista += [i]
    return lista


def lista2(): 
    return range(1000)

print(lista1())

print(len(lista1())) # O(1)

