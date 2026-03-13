
"""
Implement a program to read a matrix and multiplier and return scalar matrix multiplication.

Input Format
a 3x3 matrix and multiplier

Constraints
no

Output Format
resultent matrix

Sample Input 0
1 2 3
4 5 6
7 8 9
2
Sample Output 0
2 4 6
8 10 12
14 16 18

Sample Input 1
1 1 1
1 1 1
1 1 1
5
Sample Output 1
5 5 5
5 5 5
5 5 5

"""
l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
num = int(input())
l = [l1 ,l2 ,l3]
flage = True
for i in range(3):
    for j in range(3):
        l[i][j] =  l[i][j] * num
        print(l[i][j] ,end =' ')
    print()
    