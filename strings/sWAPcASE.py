# convert all lowercase letters to uppercase letters and vice versa.

# Author : Mahimai Raja J
# Linkedin : https://www.linkedin.com/in/mahimai-raja-j/
# Function Description
# Complete the swap_case function in the editor below.
# swap_case has the following parameters:
# string s: the string to modify

# Returns
# string: the modified string

# Input Format
# A single line containing a string .
# Constraints
# 0 < len(s) <= 1000

# Sample Input 0
# HackerRank.com presents "Pythonist 2".

# Sample Output 0
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

# X ---------------------------------------------------------------- X

def swap_case(s):
    if 0 < len(s) <= 1000:
        result = ''
        for letter in s:
            if letter.islower():
                letter = letter.upper()
                result += letter
            else:
                letter = letter.lower()
                result += letter

    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# If you have any other intresting ways comment below !