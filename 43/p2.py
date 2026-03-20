"""
Implement a program to find the unique elements present in the given array.

Input Format
size, array elements

Constraints
size<100

Output Format
print unique elements present in the array

Sample Input 0
5
1 1 2 3 4
Sample Output 0
1 2 3 4
Sample Input 1
6
1 1 1 1 1 2
Sample Output 1
1 2

"""

arr = [1 ,1 ,1 ,1 ,1 ,2]

s = set(arr)

for i in s:
    print(i ,end=' ')