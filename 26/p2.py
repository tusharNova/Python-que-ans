
"""
Write a function that takes a string name and number num (either 1 or 0) and return "Hello"+name if number is 1, otherwise "Bye"+name.

Input Format
a string from the user

Constraints
no

Output Format
a string

Sample Input 0
prakash
1
Sample Output 0
Hello prakash

Sample Input 1
java
0
Sample Output 1
Bye java
"""
st = input()
num = int(input())

if num == 1:
    print(f"Hello {st}")
else:
    print(f"Bye {st}")