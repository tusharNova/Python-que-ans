n = int(input())

lis = [int(i) for i in input().split()]
print(lis)

se , so =0 , 0
for i in lis:
    if i % 2 == 0:
        se +=i
    else:
         so +=i

print(abs(se-so))