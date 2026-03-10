"""
fibonanicaa
"""



def getFib(n: int)-> int:
    if n ==0 or n == 1:
        return n
    else:
        return getFib(n-1) + getFib(n-2)    



n = int(input("Enter number"))

print(getFib(n))