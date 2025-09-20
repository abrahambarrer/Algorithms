'''
Practice 5.2 Write a function called implode that given
a list of characters, or strings, returns a string which
is the concatenation of those characters, or strings.
'''
def implode(char_list):
    return ''.join(char_list)

def main():
    print(implode(['h', 'o', 'l', 'a']))

if __name__ == '__main__':
    main()