
def sum1(n: int) -> int:
    soma: int = 0
    for i in range(n + 1):
        soma += i
    return soma

def sum2(n) -> int: # using recursion
    if n == 0: return 0

    return n + sum2(n - 1)

if __name__ == '__main__':
    print(sum1(5))
    print(sum2(5))