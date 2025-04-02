def recursion(i: int) -> None:
    print('Recursion ', i)
    i += 1
    if i > 5:
        return
    else:
        recursion(i)

if __name__ == '__main__':
    recursion(1)