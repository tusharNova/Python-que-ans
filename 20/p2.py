"""
Accept video length in minutes the format is mm:ss in String format, create a function that takes video length and return it in seconds.

"""

n = input()

lis = n.split(":")
min = lis[0]
sec = lis[1]

print(f"total seconds is :-{(int(min)*60) + int(sec)}")