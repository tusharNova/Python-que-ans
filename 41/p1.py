"""
Implement a program to sort the given array elements in DESC order.

Input Format
size and array elements

Constraints
size<100

Output Format
sorted array in DESC

Sample Input 0
4
1 3 2 4
Sample Output 0
4 3 2 1

Sample Input 1
5
5 1 3 2 4
Sample Output 1
5 4 3 2 1
"""

n = int(input())
lis = [int(i) for i in input().split()]

lis.sort(reverse=True)
for i in lis:
    print(i ,end=' ')