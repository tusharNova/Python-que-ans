"""
Implement a program to read array elements and find the max element in an array.

Input Format
size and array elements.

Constraints
size<100

Output Format
return max element

Sample Input 0
8
1 22 33 4 8 9 88 99
Sample Output 0
99
Sample Input 1
5
1 2 3 4 5
Sample Output 1
5
"""

arr = [1, 22, 33, 4, 8, 9, 88, 99]
max_num = arr[1]

for i in arr:
    if i >max_num:
        max_num =i
    
print(max_num)