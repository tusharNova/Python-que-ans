"""
Implement a program to delete an element from an array at the position

Input Format
size,array elements and position

Constraints
size<100

Output Format
return array after deleting from the location

Sample Input 0
5
1 2 3 4 5
0
Sample Output 0
2 3 4 5

Sample Input 1
3
7 8 6
1
Sample Output 1
7 6
"""


n = int(input())
arr = [int(i) for i in input().split()]
num = int(input())
arr.pop(num)

for i in arr:
    print(i ,end=' ')