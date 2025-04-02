def potency(a: int ,b: int) -> int:
    if b == 0:
        return 1
    return a * potency(a, b - 1)

if __name__ == '__main__':
    base:int = int(input("Enter the base value: "))
    exponent:int = int(input("Enter the exponent value: "))

    print(f"{base}^{exponent} = {potency(base,exponent)}")