def main():
    filename = 'file.txt'

    # one line record
    lines = [line.strip() for line in open(filename)]

    print(lines)

    # words records
    words = [word.strip() for line in open(filename) for word in line.split() ]

    print(words)

if __name__ == '__main__':
    main()