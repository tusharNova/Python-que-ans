
"""
check for prime 
"""
n = int(input())
s = [2 ,3 ,5 ,7]
ans = 0
while n!=0:
    d = n % 10
    if d in s:
        ans = ans+ d

    n = n // 10

print(ans)
