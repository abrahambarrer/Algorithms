def reverse(lst):
    if lst == []:
        return []
    return reverse(lst[1:]) + lst[:1]


def revseq(seq):
    seq_type = type(seq)
    emptyseq = seq_type()

    if seq == emptyseq:
        return emptyseq

    return revseq(seq[1:]) + seq[:1]


def main():
    print(reverse([1, 2, 3, 4]))
    print(revseq('pomada'))


if __name__ == '__main__':
    main()
