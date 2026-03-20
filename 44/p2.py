"""
Implement a program to find the sum of two arrays and display the result array

Input Format
size and array elements

Constraints
no
Output Format
print resultent array
Sample Input 0

4
1 2 3 4
5 6 7 8
Sample Output 0
6 8 10 12

Sample Input 1
5
1 2 3 4 5
1 1 1 1 1
Sample Output 1
2 3 4 5 6

Sample Input 2
3
1 1 1
2 2 2
Sample Output 2
3 3 3
"""

n = int(input())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
arr3 = []
for i in range(n):
    arr3.append(arr1[i]+ arr2[i])
    
for i in arr3:
    print(i ,end=' ')