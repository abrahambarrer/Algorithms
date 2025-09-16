def ask_value():
    return int(input('Value: '))

def main():
    side1 = ask_value()
    side2 = ask_value()
    side3 = ask_value()

    is_perfect = 'It is a perfect triangle'

    condition1 = side1 % 3 == 0
    condition2 = side2 % 4 == 0
    condition3 = side3 % 5 == 0

    if not(condition1) or not(condition2) or not(condition3):
        is_perfect = 'It is not a perfect triangle'

    print(is_perfect)

if __name__ == '__main__':
    main()