"""
Implement a program to print min element in an matrix
"""
arr = []


for i in range(3):
    arr.append([int(i) for i in input().split()])

min_num = arr[0][0]
    
for i in range(3):
    for j in range(3):
        if min_num > arr[i][j]:
            min_num = arr[i][j]
            
print(min_num)