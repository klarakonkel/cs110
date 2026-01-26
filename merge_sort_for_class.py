"""
WHY:
the course is requiring us to code and use a specific version of merge sort (which is imo overcomplicating)
"""

def merge(A, p, q, r):
    """
    merges elements of the array A[p,...,q] with A[q+1, ..., r], assuming the two parts (sub-arrays) are seperately sorted

    Args:
    array A: array to sort
    int p: first index of left sub-array
    int q: last index of left sub-array
    int r: last index of right sub-array
    p<=q<r

    Output:
    array A: merged
    """
    left = A[p:q+1]
    right = A[q+1: r+1]
    i = 0
    j = 0
    k = p
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1
    return A

def merge_sort(A, p, r):
    
    if p>= r:
        return A #it's the base case (1 element), or an empty array

    q = (p+r) //2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)

    return A

print("test case 1: ", merge_sort([1, 2, 3, 4, 5, 6, 7, 8], 0, 7))
print("test case 2 (duplicates): ", merge_sort([1, 3, 5, 7, 2, 4, 6, 8, 2, 6], 0, 9)) 
print("test case 2 (duplicates, shortened): ", merge_sort([1, 3, 5, 7, 2, 4, 6, 8, 2, 6], 0, 7))
print("test case 3: ", merge_sort([1, 1, 1, 1, 3, 5, 7, 2, 4, 6, 8], 3, 10)) #should print sorted with an additional 1s in front
print("test case 4 (empty): ", merge_sort([], 0, 0))
