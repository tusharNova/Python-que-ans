"""
Create a function/method that takes, a word and returns true if the word has two consecutive identical letters.



Sample Input :- loop
Sample Output :- true
"""

s = input()
f = "false"

for i in range(len(s)-1):
    if s[i] ==s[i+1]:
        f="true"
        break

print(f)