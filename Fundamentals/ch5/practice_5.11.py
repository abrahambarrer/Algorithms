"""
Practice 5.11 Write the function evenlyDivisible
from Example 5.12 using the evenlyDivisibleElements
function to complete the program presented in Example
5.12 and practice Problem 5.10.
"""

def evenly_divides(x, y):
    return y % x == 0

def evenly_divisible_elements(lst, x):
    return [i for i in lst if evenly_divides(i, x)]

def evenly_divisible(lst):
    for x in lst:
        nums = evenly_divisible_elements(lst, x)
        print(f'{x} is evenly divisible by {" ".join(str(i) for i in nums)}')

def ask_values():
    s = input('Enter a list of numbers separated by spaces: ')
    return [int(i.strip()) for i in s.split()]

def main():
    nums = ask_values()
    evenly_divisible(nums)

if __name__ == '__main__':
    main()