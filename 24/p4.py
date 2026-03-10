"""
Create a function that takes a string, check if it has the same number of x's and o's and returns either true or false.
1. return boolean value true or false.
2. returns true if the amount x's and o's are the same.
3. returns false if they are not the same amount.
4. the string can contains any character.
5. when 'x' and 'o' are not in the string, return true.


Sample Input :-  ooxx
Sample Output :-  true
"""

from collections import Counter

def checkstr(st : str) ->str:
    if "x" and "o" not in st:
        return "true"
    
    xCnt , oCnt = 0 , 0
    for char in st:
        if char == "x":
            xCnt = xCnt+1
        
        if char =="o":
            oCnt = oCnt+1

    
    if xCnt == oCnt:
        return "true"

    return "false"
    

st = "ancht"

print(checkstr(st))