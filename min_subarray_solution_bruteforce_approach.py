def bruteforce_min_subarray(A):
    length = len(A)
    if length == 0:
        return "empty array"
    min_sum =  float("+inf") #same reasoning as above; assigning highest first
    start_id = 0
    end_id = 0
    for i in range (length):
        for j in range(i, length):
            s = sum(A[i:j+1])
            if s < min_sum:
                min_sum = s
                start_id = i
                end_id = j

    return (start_id, end_id, min_sum)

# testing
assert(bruteforce_min_subarray([1]*10)[0] == bruteforce_min_subarray([1]*10)[1])
assert(bruteforce_min_subarray([1]*10)[2] == 1)