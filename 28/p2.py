"""
Program to read matrix elements and find sum of all elements in the matrix.
"""
x=int(input())
y=int(input())
ary = []
nas = 0
for i in range(x):
    ary.append([int(i) for i in input().split()])


for i in range(x):
    for j in range(y):
        ans = ans + ary[i][j]
    print()