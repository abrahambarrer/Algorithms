"""
5. Write a function called allEvens that
given a list of integers, returns a new
list containing only the even integers.
Use the function in a program and test
your code on several different values.
"""

def is_even(x):
    return x % 2 == 0

def all_evens(lst):
    return [x for x in lst if is_even(x)]

def main():
    lst = [1, 5, 10, 5, 6, 9]
    print(all_evens(lst))

if __name__ == '__main__':
    main()