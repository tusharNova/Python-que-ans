"""
how many spaces in the give string
"""

n = input("")
cnt = 0
for i in n:
    if not i.isalnum():
        cnt =cnt+1


print(cnt)