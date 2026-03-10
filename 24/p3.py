"""
Create a function that takes a string and returns the number of vowels contained within it.

Sample Input 
celebration
Sample Output 
5
-------
Sample Input 
palm
Sample Output 
1
"""

vowels = ["a" ,"e" ,"i" ,"o" ,"u"]

s= input()
cnt = 0
for char in s:
    if char in vowels:
        cnt=cnt +1


print(cnt)