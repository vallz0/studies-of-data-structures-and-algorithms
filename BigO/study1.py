# Big-O Notation
import timeit

def soma1(n) -> int: # O(n)
    soma: int = 0
    for i in range(n + 1):
        soma += i

    return soma

def soma2(n) -> int: # O(3)
    return (n * (n + 1)) / 2


time1: float = timeit.timeit(lambda: soma1(10), number=100000)
print(time1)

time2: float = timeit.timeit(lambda: soma2(10), number=100000)
print(time2)


print("função 2 é mais rapida") if time2 < time1 else print("função 1 é mais rapida")


    
