""


def isprime(n:int):
    cnt = 0
    for i in range(1 ,n):
        if n %i == 0:
            cnt = cnt +1
            
    return f==2
            

ary = []
ans = 0
for i in range(3):
    ary.append([int(i) for i in input().split()])


for i in range(3):
    for j in range(3):
        # print(ary[i][j],end=' ')
        if isprime(ary[i][j]):
            ans = ans + ary[i][j]
    
print(ans)