def bubble_sort(array_to_sort):
    length = len(array_to_sort)
    j = length - 1
    while j > 0:
        last_swap = 0
        for i in range (0, j):
            if (array_to_sort[i] > array_to_sort[i+1]):
                array_to_sort[i], array_to_sort[i+1] = array_to_sort[i+1],array_to_sort[i]
                last_swap = i
        if last_swap == 0: #if we haven't swapped anything in a whole iteration then it's sorted and no need to continue with next lines
            break
        print("Currently: ", array_to_sort)
        j -= 1
    return array_to_sort

if __name__ == "__main__":
    print(bubble_sort([2, 6, 1, 8, 3, 6, 9]))