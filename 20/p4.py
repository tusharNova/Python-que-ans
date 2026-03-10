"""
Create a function that sums the total number of digits between two numbers inclusive. for example, if the numbers are 19 and 22, then (1+9)+(2+0)+(2+1)+(2+2)=19.
"""

n1 = int(input())
n2 = int(input())
s= 0
for i in range(n1 ,n2+1):
    s = s+ sum([int(j) for j in str(i)])

print(s)