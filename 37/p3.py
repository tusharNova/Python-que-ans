"""
Implement a Program to replace a character with it's occurrence in given string.

Input Format
a string and a character from the user.

Constraints
non-empty string

Output Format
replaced string

Sample Input 0
test
t
Sample Output 0
1es2

Sample Input 1
prakash
a
Sample Output 1
pr1k2sh
"""

n = 'prakash'
char = 'a'

cnt = 0
for i in n:
    if char == i:
        cnt =cnt+1
        print(str(cnt),end='')
    else: print(i ,end='')        
