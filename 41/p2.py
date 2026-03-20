"""
Implement a program to search for an element in an array.

Input Format
size, array elements and element to search

Constraints
size<100

Output Format
search for the given element

Sample Input 0
8
1 2 3 4 5 7 8 6
4
Sample Output 0
3

Sample Input 1
2
1 2
1
Sample Output 1
0
"""

"""
Solved using binary search
"""


def binary_search(arr , num):
    low ,high = 0 , len(arr) -1
    index =-1
    while low<=high:
        mid = (low+high) //2
        if num ==arr[mid]:
            index = mid
            break
        elif num > arr[mid]:
            low = mid+1
        else:
            high = mid-1
    
    return index




arr= [11 ,22 ,33 ,55 ,44]
key = 44
arr.sort()
print(binary_search(arr,key))