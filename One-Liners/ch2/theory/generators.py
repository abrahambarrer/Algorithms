def main():
    ## Data
    companies = {
        'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
        'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
        'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}
    }

    ilegal = [comp for comp in companies if any(e < 9 for e in companies[comp].values())]

    print(ilegal)

if __name__ == '__main__':
    main()