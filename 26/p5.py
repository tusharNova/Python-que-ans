"""
create a function that returns the index of first vowel in a string

Input Format
a string

Constraints
no

Output Format
an int value

Sample Input 0
apple
Sample Output 0
0

Sample Input 1
hello
Sample Output 1
1
"""
n = input()

for i in range(len(n)):
    if n[i] in ["a" ,"e" ,"i","o","u"]:
        print(i)
        break
        