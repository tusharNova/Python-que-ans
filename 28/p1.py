"""
Program to read matrix elements of order n x m and display on the console.


"""

x=int(input())
y=int(input())
ary = []
for i in range(x):
    ary.append([int(i) for i in input().split()])


for i in range(x):
    for j in range(y):
        print(ary[j][i],end=' ')
    print()