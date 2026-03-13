"""
Given a string S, the task is to remove all the duplicates in the given string.

Input Format
a string from the user

Constraints
remove all duplicates

Output Format
a string without duplicates

Sample Input 0
hello
Sample Output 0
helo

Sample Input 1
welcome
Sample Output 1
welcom
"""

n = input()

s = []

for char in n:
    if char not in  s:
        s.append(char)

print(''.join(s))