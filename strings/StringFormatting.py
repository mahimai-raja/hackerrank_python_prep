# Given an integer, n , print the following values for 
# each integer i from 1 to n:

# 1.Decimal
# 2.Octal
# 3.Hexadecimal (capitalized)
# 4.Binary

# Author : Mahimai Raja J
# Linkedin : https://www.linkedin.com/in/mahimai-raja-j/

# Function Description
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
# int number: the maximum value to print

# -------------------------------------------------

def print_formatted(number):
    width = len(f'{number:b}')
    for i in range(1, number+1):
        print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i, w=width))

        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)