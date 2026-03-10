"""
sum of digit which is divided by 3
"""


n = int(input("enter nay number " ))
s = 0 
while n!=0:
    d=n%10
    if d%3==0: 
        s+=d
    n=n//10

print(s)



