"""
Create a function/method that takes a string as a argument and returns a new string by removing all vowels from it

Sample Input :-welcome
Sample Output :- wlcm
"""
import re

print(re.sub("[aeiou]" , "" ,input()))