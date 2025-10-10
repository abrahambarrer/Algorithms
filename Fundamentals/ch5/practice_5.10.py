"""
Practice 5.10 Using the last version of the evenlyDivides function,
write a function called evenlyDivisibleElements that given an integer,
x, and a list of integers, returns the list of integers from the given
list that evenly divide x. This would be the next step in either the
bottom-up design or the top-down design of a solution to the problem
in Example 5.12.
"""

def evenly_divides(x, y):
    return y % x == 0

def evenly_divisible_elements(lst, x):
    return [i for i in lst if evenly_divides(i, x)]

def main():
    print(evenly_divisible_elements([1, 2, 3, 5, 6, 7, 8], 10))

if __name__ == '__main__':
    main()