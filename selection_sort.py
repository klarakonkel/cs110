def selection_sort(array_to_sort):
    length = len(array_to_sort)
    for i in range (0, length -1):
        current_min = i
        j = i + 1
        while j < length:
            if array_to_sort[current_min] > array_to_sort[j]:
                current_min = j
            j += 1
        if current_min != i:
            array_to_sort[i], array_to_sort[current_min] = array_to_sort[current_min], array_to_sort[i]
        print("Swap: ", array_to_sort)
    return array_to_sort


if __name__ == "__main__":
    print(selection_sort([3, 5, 2, 8, 1 ,6, 9]))