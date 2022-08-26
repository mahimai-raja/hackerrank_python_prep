# You are given an integer, . Your task is to print 
# an alphabet rangoli of size . (Rangoli is a form of 
# Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# The center of the rangoli has the first alphabet 
# letter a, and the boundary has the  alphabet letter (in alphabetical order).

# Function Description
# Complete the rangoli function in the editor below.

# rangoli has the following parameters:
# int size: the size of the rangoli

# Returns
# string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

# ------------------------------------------------

def print_rangoli(size):
    import string
    design = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)