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

if __name__ == "__main__":
    print("test case 1: ", merge_sort[1, 4, 5, 9, 2, 8, 3, 6]))
    print("test case 2 (duplicate): ", merge_sort([1, 4, 5, 9, 2, 8, 3, 6, 5]))
    print("test case 3 (empty): ", merge_sort([]))