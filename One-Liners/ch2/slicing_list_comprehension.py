def main():
    ## Data (daily stock prices ($))
    price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
             [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
             [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
             [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

    # Every other value in different lists
    lst = [line[::2] for line in price]

    print(lst)

    # Every other value all in the same list
    lst = [e for line in price for e in line[::2]]

    print(lst)

if __name__ == '__main__':
    main()