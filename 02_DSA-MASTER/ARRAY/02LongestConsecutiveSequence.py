def longest_consecutive_sequence(arr):
    num_set = set(arr)
    print(num_set)
    longest_streak = 0
    # longest_arr = []


    for num in num_set:
        if not num-1 in num_set:
            lenght = 0
            arrs = []

            while num+lenght in num_set:
                arrs.append(num+lenght)
                lenght += 1
            # arrs.append(num+lenght)
            # longest_streak = max(lenght, longest_streak)

            if lenght > longest_streak:
                longest_streak = lenght
                lenght = longest_streak
                longest_arr = arrs
            # return longest_streak




    

    return longest_streak, longest_arr

arr = [1, 9, 3, 10, 4, 20, 2]
print(longest_consecutive_sequence(arr))  # Output: 4 (for the sequence [1, 2, 3, 4])
