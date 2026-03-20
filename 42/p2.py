"""
Implement a program to delete an element from an array at the first position

Input Format
size,array elements

Constraints
size<100

Output Format
return array after deleting from first location

Sample Input 0
5
1 2 3 4 5
Sample Output 0
2 3 4 5

Sample Input 1
3
11 87 25
Sample Output 1
87 25
"""

n = int(input())
arr = [int(i) for i in input().split()]

arr.pop(0)

for i in arr:
    print(i ,end=' ')