def main():
    ## Data
    visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
                'Safari', 'corrupted', 'Safari', 'corrupted',
                'Chrome', 'corrupted', 'Firefox', 'corrupted']

    visitors[1::2] = visitors[::2]

    print(visitors)

if __name__ == '__main__':
    main()