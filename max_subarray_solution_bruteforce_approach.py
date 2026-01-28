def bruteforce_max_subarray(A):
    length = len(A)
    if length == 0:
        return "empty array"
    max_sum =  float("-inf") #the reason I'm defining max sum differently than sum = 0 is because for an array of negative numbers, we wouldn't be able to assign the max value correctly because in line , the sum would never be higher than 0; so im assigning the smallest possible value aka most negative int
    start_id = 0
    end_id = 0
    for i in range (length):
        for j in range(i, length):
            s = sum(A[i:j+1])
            if s > max_sum:
                max_sum = s
                start_id = i
                end_id = j

    return (start_id, end_id, max_sum)


if __name__ == "__main__":
    print(bruteforce_max_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
    print(bruteforce_max_subarray([]))
    print(bruteforce_max_subarray([9]))