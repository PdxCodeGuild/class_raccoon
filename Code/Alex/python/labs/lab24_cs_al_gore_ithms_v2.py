'''
Lab 24: Computer Science - Algorithms

Version 2 - Binary Search

Implement binary search, which requires that a list is sorted. Begin by defining two indices: low and high. Initialize low as the lowest index in the list and high as the highest. Loop while low is less then high. For each iteration, calculate a third index mid which is in the middle between low and high. If the element at mid is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at mid. If it's less, make high equal to mid and loop. If it's greater, make low equal to mid and loop. If the loop terminates without returning, return a value indicating that it was not found.

Example run:

 L        M           H
[1, 2, 3, 4, 5, 6, 7, 8]
 L  M     H
[1, 2, 3, 4, 5, 6, 7, 8]
    L  M  H
[1, 2, 3, 4, 5, 6, 7, 8]
Psuedocode:

// A - the list
// n - the length of the list
// T - the value we're searching for
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful
Stub:

def binary_search(nums, value):
  ...
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
'''


def binary_search(nums, value):
    L = 0
    R = (len(nums) - 1)
    while L <= R:
        m = (L + R)//2
        if nums[m] < value:
            L = m + 1
        elif nums[m] > value:
            R = m -1
        else:
            return m
    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 3)
print(index) # 2