"""
Andy, Ben and Charlotte are playing a board game. the three of them decided to come up with a new scoring system. A player's first initial ("A","B" and "C") denotes that players scoring a signle point. Given a string of capital letters. return an array of the player's score.


Sample Input :- A
Sample Output :- 1 0 0
"""


s = input()
print(s.count('A') ,s.count('B') ,s.count('C'))