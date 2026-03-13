"""
Program to accept a matrix and check whether it is upper triangular matrix or not

"""

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]

l = [l1 ,l2 ,l3]
flage = True
for i in range(3):
    for j in range(3):
        if j<i and l[i][j] !=0:
            flage =False

print("Yes" if flage else "No")