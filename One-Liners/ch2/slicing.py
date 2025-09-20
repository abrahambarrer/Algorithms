def main():
    ## Data
    letters_amazon = '''
    We spent several years building our own database engine, 
    Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible 
    service with the same or better durability and availability as 
    the commercial engines, but at one-tenth of the cost. We were 
    not surprised when this worked.
    '''

    find = lambda txt, strng: txt[txt.find(strng)-18:txt.find(strng)+18] if strng in txt else -1

    print(find(letters_amazon, 'SQL'))

if __name__ == '__main__':
    main()