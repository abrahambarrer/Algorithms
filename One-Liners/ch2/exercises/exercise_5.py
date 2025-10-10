"""
Tienes la lista ['Hola Mundo', 'Python', 'lambda'].
Usa map y lambda para devolver una lista de booleanos
indicando si cada cadena contiene la letra "o".
"""

def main():
    mylist = ['Hola Mundo', 'Python', 'lambda']

    # Using lambda
    contain_o = list(map(lambda s: 'o' in s, mylist))

    # Not lambda
    contain_o2 = [('o' in s) for s in mylist]

    print(contain_o)

if __name__ == '__main__':
    main()