'''
Computer Science - Algorithms
Version 5 - Quicksort

Quicksort is one of the most efficient sorting algorithms. It works by swapping elements on either side of a pivot value.

Psuedocode:

algorithm quicksort(A) is
    quicksort_recursive(A, 0, length(A) - 1)

algorithm quicksort_recursive(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort_recursive(A, lo, p)
        quicksort_recursive(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[lo + (hi - lo) / 2]
    i := lo - 1
    j := hi + 1
    loop forever
        do
            i := i + 1
        while A[i] < pivot
        do
            j := j - 1
        while A[j] > pivot
        if i ≥ j then
            return j
        swap A[i] with A[j]

'''

def quicksort(nums):
    quicksort_recursive(nums, 0, len(nums)-1)












nums = [1, 0, 9, 100, 1, 0, 2, 5, 3, 4, 5, 6, -1, 7, 9, 8, 10, 2, 20]

print(nums)
quicksort(nums)
print(nums)
