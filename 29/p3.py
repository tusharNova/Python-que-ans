"""
Implement a program to print transpose of a matrix

"""


arr = []

for i in range(3):
    arr.append([int(i) for i in input().split()])
    
    
for i in range(3):
    for j in range(3):
        print(arr[j][i] ,end=' ')
    print()