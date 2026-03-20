"""
Implement a program to find the sum of elements avaiable at even index locations in an array.

Input Format
size and array elements

Constraints
no

Output Format
print sum value

Sample Input 0
5
1 2 3 4 5
Sample Output 0
9

Sample Input 1
5
1 1 1 1 1
Sample Output 1
3
Sample Input 2
6

1 2 3 4 5 6
Sample Output 2
9
"""


n = int(input())
arr = [int(i) for i in input().split()]
total = 0
for i in range(n):
    if i %2==0:
        total += arr[i]
    
print(total)