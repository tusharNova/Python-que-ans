"""
Q) Two Strings a and b are called anagrams, if they contain all the same characters in the same frequencies
-----
Sample Input 0
anagram
margana

Sample Output 0
true
--------
Sample Input 1
python
java

Sample Output 1
false
"""

# Less Efficient Method: Using sorted() (O(n log n)) 
str1 = input()
str2 = input()

print("true" if sorted(str1) == sorted(str2) else "false")



# Alternative O(n) Method: Using a Single Dictionary 

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if len(str1) != len(str2):
    print("false")

cunt_map = {}
for char in str1:
    cunt_map[char] = cunt_map.get(char , 0) +1


for char in str2:
    if char not in cunt_map or cunt_map[char] == 0:
        print("false")
        break
    cunt_map[char] -= 1

print("true")