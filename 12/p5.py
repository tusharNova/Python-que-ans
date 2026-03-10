"""
for Niven number
"""

n = int(input())
# s = [2 ,3 ,5 ,7]
ans = 0
while n!=0:
    d = n % 10
    ans = ans+ d
    n = n // 10


print("is Niven" if n % ans ==0 else "this not")