"""
Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, return the original uncensored string.

Input Format
censored string and removed vowels as string

Constraints
non-empty string

Output Format
updated string

Sample Input 0
w*lc*m*
eoe
Sample Output 0
welcome

Sample Input 1
Wh*r* d*d my v*w*ls g*?
eeioeo
Sample Output 1
Where did my vowels go?
"""

s1 = input()
s2 = input()
j=0
for i in s1:
    if i =="*":
        print(s2[j],end='')
        j+=1
    else:
        print(i , end='')
