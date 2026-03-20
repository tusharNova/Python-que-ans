"""
Implement a program to read an array elements and print sum of all odd elements.

Input Format
size of the array and array elements

Constraints
size<100

Output Format
sum of all odd elements

Sample Input 0
5
1 2 3 4 5
Sample Output 0
9
Sample Input 1
8
1 2 3 8 5 2 7 3
Sample Output 1
19

Sample Input 2
4
11 22 33 44
Sample Output 2
44
"""

n = int(input())
li = [int(i) for i in input().split()]
total = 0
for num in li:
    if num %2 !=0:
        total +=num
        
print(total)