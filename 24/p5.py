"""
write a function that shutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... , and then the word is pronounced with a question mark?



Sample Input :- incredible
Sample Output :- in...in...incredible?
"""


s = input()
print(f"{s[0]+s[1]}...{s[0]+s[1]}...{s}")