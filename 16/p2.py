n = int(input())
ans = 0

while n !=0:
    d = n %10
    if d % 2!=0:
        ans =ans + d

    n = n //10

print(ans)
