"""
prime or not
"""


n = int(input())
fact = 0
for i in range(1 , n+1):
    if n %i == 0:
        fact+=1

print("prime " if fact == 2 else "not")