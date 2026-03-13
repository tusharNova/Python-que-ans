"""
Write a Java program to take an input string and exchange the first and last word and reverse the middle word.

Input Format
a string

Constraints
no

Output Format
a string

Sample Input 0
Hello welcome to java

Sample Output 0
java ot emoclew Hello
"""

# n = "Hello welcome to java"

n = input()
lis = n.split()
print(lis[-1] ,end=' ')

for i in range(len(lis)-2 , 0 ,-1):
    print(lis[i][::-1] ,end=' ')


print(lis[0])
