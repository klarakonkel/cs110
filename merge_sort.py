f"""
PSEUDOCODE:
mergesort(array a)
-> divides array into 2x half arrays recursively until they are one element each

merge(array1, array2)

while a and b have elements:

    if a[0] > b[0]
        add b[0] to the end of c
        remove b[0] from b

    else (if a[0] < b[0])
        add a[0] to the end of c
        remove a[0] from a

//when loop ends, either a or be is empty
while a has elements
    add a[0] to the end of c
    remove a[0] from a
while b has elements
    add b[0] to the end of c
    remove b[0] from b

return c
"""

def break_down(array_to_break_down):
    length = len(array_to_break_down)
    if length <= 1:
        return array_to_break_down
    mid = length //2
    first_half = break_down(array_to_break_down[:(length//2)])
    second_half = break_down(array_to_break_down[(length//2):])

    return merge_sort(first_half, second_half)


def merge_sort(array_one, array_two):
    merged = []
    i_one = 0
    i_two = 0

    while i_one < len(array_one) and i_two < len(array_two):
        if array_one[i_one] < array_two[i_two]:
            merged.append(array_one[i_one])
            i_one += 1
        else:
            merged.append(array_two[i_two])
            i_two += 1
    #when one of the arrays have reached end:
    while i_one < len(array_one):
        merged.append(array_one[i_one])
        i_one += 1
    while i_two < len(array_two):
        merged.append(array_two[i_two])
        i_two += 1
    #according to pcw an if would do; but isn't there a case where the whole right array could be added before the left, like if we had [4,7] and [1, 3], then we want [1,3,4,7], so we'd place [1,3] and the second array would be empty but we'd still have [4,7] in the first array, no?

    return merged

if __name__ == "__main__":
    print("test case 1: ", break_down([1, 4, 5, 9, 2, 8, 3, 6]))
    print("test case 2 (duplicate): ", break_down([1, 4, 5, 9, 2, 8, 3, 6, 5]))
    print("test case 3 (empty): ", break_down([]))