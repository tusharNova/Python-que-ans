"""
Implement a program to insert an element into an array at the last position

Input Format
size,array elements and element to be inserted

Constraints
size<100

Output Format
return array after insertion

Sample Input 0
5
1 2 3 4 5
10
Sample Output 0
1 2 3 4 5 10

"""

n = int(input())
arr = [int(i) for i in input().split()]

arr.append(int(input()))
for i in arr:
    print(i , end=' ')