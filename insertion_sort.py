def insertion_sort(array_to_sort):

    arr_length =len(array_to_sort)
    temp = 0

    for i in range (1, arr_length):
        j = i - 1
        key = array_to_sort[i]
        while j >= 0 and array_to_sort[j] > key:
            array_to_sort[j + 1] = array_to_sort[j]
            j -= 1
        array_to_sort[j + 1] = key
        print("inserted:", array_to_sort)
    return array_to_sort



if __name__ == "__main__":
    print(insertion_sort([7,9,3,6,2,5,1,4,2]))