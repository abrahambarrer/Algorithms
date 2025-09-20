'''
Practice 5.1   Write a function called explode that given
a string returns a list of the characters of the string.
'''

def explode(s):
    return [char for char in s]

def main():
    print(explode('Hello world'))

if __name__ == '__main__':
    main()