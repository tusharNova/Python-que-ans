"""
Given a valid IP address, return a defanged version of that IP address. A defanged IP address replaces every period '.' with "[.]".
"""

n = input()
ans = n.replace(".","[.]")
print(ans)