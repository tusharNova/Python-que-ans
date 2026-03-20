"""
Given a string containing unique letters, return a sorted string with the letters that don't appear in the string.

Input Format
A string from the user

Constraints
non empty string

Output Format
return missing characters in the given string

Sample Input 0
abcdefgpqrstuvwxyz
Sample Output 0
hijklmno

Sample Input 1
zyxwvutsrq
"""

st = input()

for i in range(97 , 123):
    n = chr(i)
    if n is not st:
        print( n ,end='')