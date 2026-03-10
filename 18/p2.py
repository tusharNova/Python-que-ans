import math

def isprime(n : int):
    cnt = 0
    for i in range(1 ,n +1):
        if n % i  ==0:
            cnt =cnt+1

    return cnt == 2




n1 = int(input())
n2 = int(input())
sum = 0


for i in range(n1 ,n2+1):
    if isprime(i):
        sum = sum +i

print(sum)