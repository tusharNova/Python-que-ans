"""
Create a function/method that takes a string and returns a string in which each character is repeated once


Sample Output :-hello
Sample Input :- hheelllloo
"""

s = input()
ans = ""
for char in s:
    ans =ans + char*2

print(ans)