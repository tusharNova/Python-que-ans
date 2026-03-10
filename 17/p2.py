n = input()
cnt = 0

for i in n:
    if i.isalnum() or i.isspace():
        continue
    else: cnt = cnt + 1

print(cnt)