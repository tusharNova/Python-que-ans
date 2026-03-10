"""
Given a string s, and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string, return shuffled string.

Sample Input 
Hello

Sample Output 
lololo
"""
s = input()
a =[int(i) for i in input().split()]
b = [0] * len(s)

for i in range(0 , len(s)):
    b[a[i]] = s[i]
    
print(''.join(b))
# print(st)