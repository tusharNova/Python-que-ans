"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid. Formally, a parentheses string is valid if and only if: It is the empty string, or It can be written as AB (A concatenated with B), where A and B are valid strings, or It can be written as (A), where A is a valid string. Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Input Format
string from the user

Constraints
non-empty string

Output Format
minimum number of ( or ) required.

Sample Input 0
()
Sample Output 0
0

Sample Input 1
()(
Sample Output 1
1
"""

s = input()
cnt = 0
for char in s:
    if char =='(':
        cnt+=1
    if char==')':
        cnt-=1

print(cnt)
