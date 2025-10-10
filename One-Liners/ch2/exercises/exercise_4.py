"""
Genera todas las combinaciones posibles de
dos listas: [1, 2, 3] y ['a', 'b'], como
tuplas (número, letra).
"""

def main():
    list1 = [1, 2, 3]
    list2 = ['a', 'b']

    permut = [(num, char) for num in list1 for char in list2]

    print(permut)

if __name__ == '__main__':
    main()