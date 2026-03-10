"""
Write a function that finds the word "bomb" in the given string (not case sensitive). Return "DUCK!" if found, otherwise,"Relax, there's no bomb.".
"""
s = input()

if "bomb" in  s.lower():
    print("DUCK!")
else: 
    print("Relax, there's no bomb.")