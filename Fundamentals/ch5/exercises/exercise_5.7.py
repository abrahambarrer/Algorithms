"""
7. Write a function called isPrime
that returns True if an integer given
to the function is a prime number. Use
the function in a program and test
your code on several different values.
"""

import math

def is_prime(x):
    if x <= 1:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def main():
    print(is_prime(121))

if __name__ == '__main__':
    main()