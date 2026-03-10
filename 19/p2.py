"""
perfect number
"""


n = int(input())
s = 0
for i in range(1,n):
    if  n % i==0:
        s = s+i 


print("ture" if s==n else "false")