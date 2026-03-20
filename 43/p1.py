"""
Implement a program to find the number of duplicate elements present in the given array.

Input Format
size, array elements

Constraints
size<100

Output Format
number of duplicate elements in the array

Sample Input 0
5
1 1 2 2 3
Sample Output 0
2

Sample Input 1
4
1 1 1 2
Sample Output 1
1
"""

arr = [1 ,1 ,2 ,2 ,3]

dic ={}
cnt=0
for i in arr:
    dic[i] = dic.get(i,0) + 1

print(dic)
for i in dic.values():
    if i >=2: cnt+=1

print(cnt)
