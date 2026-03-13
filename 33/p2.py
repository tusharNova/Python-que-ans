"""
Implement a program to find sum of odd indexed rows in the given matrix.

Input Format
a 3x3 matrix

Constraints
no

Output Format
sum as an int

Sample Input 0
1 2 3
4 5 6
7 8 9
Sample Output 0
15

Sample Input 1
1 0 0
0 1 0
0 0 1
Sample Output 1
1
"""


l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]

l = [l1 ,l2 ,l3]
total = 0
for i in range(3):
    for j in range(3):
        if j % 2!=0:
            total += l[i][j] 

print(total)