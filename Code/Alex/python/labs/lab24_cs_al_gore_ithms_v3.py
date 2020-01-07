'''
Lab 24: Computer Science - Algorithms

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