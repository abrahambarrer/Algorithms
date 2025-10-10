"""
4. Write a predicate function called isEven
 that returns True if a number is even and
 False if it is not. Use the function in a
 program and test your code on several different
 values.
"""

def is_even(x):
    return x % 2 == 0

def main():
    for i in range(10):
        print(i, is_even(i))

if __name__ == '__main__':
    main()