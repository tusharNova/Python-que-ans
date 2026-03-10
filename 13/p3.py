"""
ind then values ::::: i + (i+1)+ (i+2)+ (i+3) ,,,, j+ (j-1)+ (j-2)+ (j-3) ... +k
"""
i = int(input())
j = int(input()) 
k = int(input())

sum = 0
while i<= j:
    sum = sum+i
    i = i+ 1

while j!= k:
    j = j-1
    sum = sum +j
    
print(sum)