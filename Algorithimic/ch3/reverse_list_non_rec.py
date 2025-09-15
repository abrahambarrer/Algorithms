def reverse(lst):
    acumulator = []

    for i in range(len(lst)-1, -1, -1):
        acumulator.append(lst[i])

    return acumulator

def main():
    print(reverse([1, 2, 3, 4]))

if __name__ == '__main__':
    main()