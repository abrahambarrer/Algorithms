"""
Con la cadena "PythonOneLiners", obtén solo
los caracteres que estén en posiciones pares.
"""

def main():
    strng = 'PythonOneLiners'

    # Indexes with even numbers
    pairs = strng[::2]

    print(pairs)

if __name__ == '__main__':
    main()