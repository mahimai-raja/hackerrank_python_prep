# In this challenge, the user enters a string and a 
# substring. You have to print the number of times that 
# the substring occurs in the given string. 
# String traversal will take place from left to right, 
# not from right to left.

# NOTE: String letters are case-sensitive.

# -------------------------------------------------------


def count_substring(string, sub_string):
    count = 0
    n = 0
    slen = len(string)
    sublen = len(sub_string)
    for i in range(slen-sublen+1):
        if sub_string == string[n:sublen+n]:
            count += 1
        n += 1
    return  count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)