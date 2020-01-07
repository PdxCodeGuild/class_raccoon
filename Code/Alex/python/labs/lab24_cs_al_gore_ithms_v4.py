'''
Lab 24: Computer Science - Algorithms

Version 4 - Insertion Sort

Implement insertion sort, which like bubble sort is also O(n^2), but is efficient at placing new values into an already-sorted list.

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