def factorial(m: int):
    if m == 0:
        return 1
    return m * factorial(m - 1)

if __name__ == '__main__':
    n: int = int(input("Enter a number to calculate factorial: "))
    print(f"{n}! = {factorial(n)}")