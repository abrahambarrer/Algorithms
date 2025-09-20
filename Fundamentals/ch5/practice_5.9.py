def evenly_divides_list(lst, x):
    return all(e % x == 0 for e in lst)

def main():
    print(evenly_divides_list([6, 2, 10, 4], 2))

if __name__ == '__main__':
    main()