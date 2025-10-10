import re

def main():
    text = '''A blockchain, originally block chain, 
    is a growing list of records, called blocks, 
    which are linked using cryptography.
    '''

    print(re.findall('b...k', text))

    print(re.findall('y.*y', text))

if __name__ == '__main__':
    main()