"""
Practice 5.15 Write a recursive function that
computes the nth Fibonacci number. The Fibonacci
numbers are defined as follows:
Fib(0) = 1,
Fib(1) = 1,
Fib(n) = Fib(n − 1) + Fib(n − 2).
Write this as a Python function and then write some
code to find the tenth Fibonacci number.
"""

def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

def main():
    print(fib(5))

if __name__ == '__main__':
    main()