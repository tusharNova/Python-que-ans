n = int(input())
se  ,so = 0 , 0
while n!=0:
    d = n %10
    if d % 2==0:
        se =se +d
    else: so =so +d

    n = n//10


print(se *so)
    
