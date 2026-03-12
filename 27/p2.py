"""
Implement a program that returns the number of decimal places a number (given as a string) has. Any zeros after the decimal point count towards the number of decimal places.

Input Format
string from the user

Constraints
non empty string

Output Format
count of decimal places

Sample Input 0
43.20
Sample Output 0
2

Sample Input 1
400
Sample Output 1
0

"""

n = input()
lis = n.split(".")

print(lis[1][0])
