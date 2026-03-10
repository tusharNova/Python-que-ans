"""
Given s string, implement a program to find max occurring character in the given string.

Sample Input 
aabbbccccddddd

Sample Output 
d
"""
from collections import Counter

n = input()

s = Counter(n)

print(max(s , key=s.get))