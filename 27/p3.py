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
"""


st = input()
res = []
seen= set()
for char in st:
    if char not in seen:
        res.append(char)
        seen.add(char)


print(''.join(res))