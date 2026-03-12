"""
Write a program to find sum of all even elements in the matrix.
"""


ary = []
ans = 0
for i in range(3):
    ary.append([int(i) for i in input().split()])


for i in range(3):
    for j in range(3):
        # print(ary[i][j],end=' ')
        if ary[i][j] % 2==0:
            ans = ans + ary[i][j]
    print()