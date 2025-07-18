def sum_n_integers(n):
    if n == 0:
        return 0
    return sum_n_integers(n-1) + n

def main():
    n = int(input('Insert a non-negative value: '))
    recursive_sum = sum_n_integers(n)
    print(f'The sum of first n integers is {recursive_sum}')

if __name__ == '__main__':
    main()