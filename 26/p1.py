"""
Create a function that replaces all the vowels in a string with a specified character,

Input Format
A string from the user

Constraints
No

Output Format
A string

Sample Input :- 
welcome
#
Sample Output :-w#lc#m#
"""

import re
s1 = input()
s2 = input()

print(re.sub("[aeiou]" , s2 ,s1))