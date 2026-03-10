"""
next prime
"""
def isprime(num: int) -> bool:
    cnt = 0
    for i in range(1 , num+1):
        if num %i ==0:
            cnt+=1

    return cnt == 2


n = int(input())

while(True):
    if isprime(n):
        print(f"The next prime no. is {n}")
        break
    n+=1

