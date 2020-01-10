'''
Computer Science - Algorithms
Version 4 - Insertion Sort

Implement insertion sort, which like bubble sort is also O(n^2),
but is efficient at placing new values into an already-sorted list.

Psuedocode:

i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while

'''

def insertion_sort(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
        i += 1

nums = [1, 0, 9, 100, 1, 0, 2, 5, 3, 4, 5, 6, -1, 7, 9, 8, 10, 2, 20]

print(nums)
insertion_sort(nums)
print(nums)
