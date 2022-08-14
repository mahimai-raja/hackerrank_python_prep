# Author : Mahimai Raja J
# Linkedin : https://www.linkedin.com/in/mahimai-raja-j/

# Task 
# Given an integer, , and  space-separated integers as input, 
# create a tuple, , of those  integers. Then compute and print the result of hash().

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format:
# The first line contains an integer n, , denoting the number of elements in the tuple. 
# The second line contains  n space-separated integers describing the elements in tuple t.

# Output Format:
# Print the result of hash().

# Sample Input 
# 2
# 1 2

# Sample Output
# 3713081631934410656

# --------------------------------------------------------------------- #

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    int_tuple = tuple(integer_list)
    print(hash(int_tuple))

# TIPS : 
# 1. hash() function can be used only on immutable objects only.
# 2. hash() of an int returns same values.