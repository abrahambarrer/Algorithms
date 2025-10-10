"""
Escribe un one-liner que lea un archivo
nombres.txt y guarde cada línea en una
lista sin saltos de línea.
"""

def main():
    file_name = 'nombres.txt'

    records = [line.strip() for line in open(file_name)]

    print(records)
    
if __name__ == '__main__':
    main()