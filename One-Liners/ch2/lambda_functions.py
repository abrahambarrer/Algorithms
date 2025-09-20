def main():
    ## Data
    txt = ['lambda functions are anonymous functions.',
           'anonymous functions dont have a name.',
           'functions are objects in Python.']

    # Map function maps every element of an iterator with the result of
    # the function applied to elements of the list
    mark = map(lambda s : ('anonymous' in s, s), txt)

    print( list(mark) )

if __name__ == '__main__':
    main()