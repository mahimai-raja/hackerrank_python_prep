# Author : Mahimai Raja J
# Linkedin : https://www.linkedin.com/in/mahimai-raja-j/
# Task 
# Read a given string, change the character at a given index 
# and then print the modified string. 

# Function Description
# Complete the mutate_string function in the editor below.
# mutate_string has the following parameters:

# string string: the string to change
# int position: the index to insert the character at
# string character: the character to insert

# Returns
# string: the altered string

# -------------------------------------------------------

def mutate_string(string, position, character):
    LIST = list(string)
    LIST[position] = str(character)
    string = ''.join(LIST)
    return string
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)