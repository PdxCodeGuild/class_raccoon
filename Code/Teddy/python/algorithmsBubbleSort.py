'''
Computer Science - Algorithms
Version 3 - Bubble Sort

Bubble sort is one of the simplest and least efficient sorting algorithms. We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.

procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped = false
        for i := 1 to n - 1 inclusive do
            /* if this pair is out of order */
            if A[i - 1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i - 1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure

'''

def bubble_sort(nums):
    num_len = len(nums)
    swapped = True
    while swapped:
        swapped = False
        i = 1
        for i in range(1, num_len):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapped = True

nums = [1, 0, 9, 1, 0, 2, 5, 3, 4, 5, 6, 7, 9, 8, 10, 2, 20]

print(nums)
bubble_sort(nums)
print(nums)
