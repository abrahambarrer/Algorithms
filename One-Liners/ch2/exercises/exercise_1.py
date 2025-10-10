"""
Dado un diccionario con los nombres y edades
de estudiantes, crea una lista con los nombres
de los que tienen 18 años o más.
"""

def main():
    example = {
        'Loeza' : 17,
        'Fernando' : 20,
        'Josue' : 21,
        'Nicole' : 20
    }

    adults = [people for people, age in example.items() if age >= 18]

    print(adults)

if __name__ == '__main__':
    main()