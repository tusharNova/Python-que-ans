"""
blackjack ...
"""

def blackjack(n1 : int , n2:int) ->int:
    if n1>21 and n2>21:
        return 0
    
    if n1 > 21:
        return n2
    elif n2> 21:
        return n1
    else:
        return max(n1 ,n2)
    

n1 = int(input())
n2 = int(input())

print(blackjack(n1 ,n2))