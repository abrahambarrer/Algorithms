"""
6. Write a function called isPalindrome
 that returns True if a string given to
 it is a palindrome. A palindrome is a
 string that is the same spelled backwards
 or forwards. For instance, radar is a
 palindrome. Use the function in a program
 and test your code on several different
 values.
"""

def is_palondrome(str):
    reverse = "".join(i for i in str[-1::-1])
    return str == reverse

# feedback ia
def isPalindrome(str):
    return str == str[::-1]

# low level
def palindrome(str):
    left, right = 0, len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    print(is_palondrome("adan nada "))

if __name__ == '__main__':
    main()