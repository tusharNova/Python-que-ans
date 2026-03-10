"""
Covetor
"""

n = input()

lis = n.split(":")
min = lis[0]
sec = lis[1]

print(f"total seconds is :-{(int(min)*60) + int(sec)}")