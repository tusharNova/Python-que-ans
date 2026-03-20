"""
Implement a program to read an array and sort array elements with 0s, 1s and 2s.

Input Format
size, array elements

Constraints
size<100

Output Format
print sorted elements

Sample Input 0
3
1 0 2
Sample Output 0
0 1 2
Sample Input 1
4
1 0 1 2
Sample Output 1
0 1 1 2
"""

arr = [1 ,0 ,1 ,2]

arr.sort()
for i in arr:
    print(i,end=' ')