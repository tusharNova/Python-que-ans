"""
sum of the even values
"""

n1 = int(input())
n2 = int(input())
ans = 0
for i in range(n1 ,n2+1):
    if i %2 == 0:
        ans +=i

print(ans)
        