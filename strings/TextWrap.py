# Question 

# You are given a string  and width . 
# Your task is to wrap the string into a paragraph of width .

# Function Description
# Complete the wrap function in the editor below.
# wrap has the following parameters:
# string string: a long string
# int max_width: the width to wrap to

# Returns
# string: a single string with newline characters ('\n') 
# where the breaks should be


# ---------------------------------------------------


import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width).fill(text=string)
    return wrapper

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)