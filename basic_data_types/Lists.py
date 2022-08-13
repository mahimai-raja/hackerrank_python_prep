# Consider a list (list = []). You can perform the following commands:
# Author : Mahimai Raja J
# Linkedin : https://www.linkedin.com/in/mahimai-raja-j/

# X --------------------------- Question ---------------------------X

# 1. insert i e: Insert integer  at position .
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer .
# 4. append e: Insert integer  at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of  followed by  lines of 
# commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding 
# operation on your list.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

# X ----------------------------------------------------------------- X

if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range(0,N):
        cmd = input().split(' ')
        if cmd[0] == 'append':
            List.append(int(cmd[1]))
        elif cmd[0] == 'insert':
            List.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'remove':
            List.remove(int(cmd[1]))   
        elif cmd[0] == 'sort':
            List.sort()
        elif cmd[0] == 'pop':
            List.pop()
        elif cmd[0] == 'reverse':
            List.reverse()
        elif cmd[0] == 'print':
            print(List)
