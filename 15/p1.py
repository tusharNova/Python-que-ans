"""
"""
n1 = [int(i) for i in input()]
n2 = [int(i) for i in input()]
n3 = [int(i) for i in input()]


d1 = min(n1[2] , n2[2] , n3[2] )
d2 = min(n1[1] , n2[1] , n3[1] )
d3 = min(n1[0] , n2[0] , n3[0] )
d4 = max(max(n1) , max(n2) , max(n3))


print(f"the pin is {d4}{d3}{d2}{d1}")
