def longest_consecutive_sequence(arr):
    set_arr = set(arr)
    max_sequnce = 0

    for num in set_arr:
        if num-1 not in set_arr:
            curr_sequence = 0
            while num+curr_sequence in set_arr:
                curr_sequence+=1

            max_sequnce = max(curr_sequence, max_sequnce)
    return max_sequnce

# arr = [11, 1, 9, 3, 10, 4, 20, 2]
arr = [1, 9, 3, 10, 4, 20, 2]
sequence = longest_consecutive_sequence(arr)
print(sequence)

