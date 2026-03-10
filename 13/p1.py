
n  = int(input())

a = n %10
b = (n//10) %10

c = (a+b) + (a*b)

print("yes" if c == n else "No")
 