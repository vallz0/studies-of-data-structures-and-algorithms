

lista: list[int] = [1, 2, 3, 4, 5]

def constant(n): # O(1) - Constant
    print(n[0])


def linear(n): # O(n) - Linear
    for i in n:
        print(i)


def quadratic(n): # O(n**2) - Quadratic 
    for i in n:
        for j in n:
            print(i,j)
        print('--')

# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)
def combination(n): # O(n)
    # O(1)
    print(n[0])

    # O(5)
    for i in range(5):
        print('teste ', i)

    # O(n)
    for i in n:
        print(i)
        
    # O(n)
    for i in n:
        print(i)

    # O(3)
    print('Python')
    print('Python')
    print('Python')


        
