import math
"""The Challenge
Calculate the volume of a right circular cone.

Input
The input consists of two lines of text.
The first line contains integer r, the
radius of the cone. The second line contains
integer h, the height of the cone. Both
r and h are between 1 and 100. (That is,
the minimum value for r and h is 1, and
the maximum value is 100.)

Output
Output the volume of the right circular cone
with radius r and height h. The 2 formula
to calculate the volume is (π * r^2 * h)/3
"""

def main():
    radius = int(input())
    height = int(input())

    volume = (math.pi * radius**2 * height) / 3
    print(volume)

if __name__ == '__main__':
    main()