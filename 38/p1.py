"""
Program to find first non-repeated character

Input Format
a non-empty string from the user

Constraints
no

Output Format
non-repeated character

Sample Input 0
aabcdbe
Sample Output 0
c
Sample Input 1
prakash
Sample Output 1
p

Sample Input 2
indian
Sample Output 2
d
"""

s = input()
for i in s:
    if s.count(i) ==1:
        print(i)
        break