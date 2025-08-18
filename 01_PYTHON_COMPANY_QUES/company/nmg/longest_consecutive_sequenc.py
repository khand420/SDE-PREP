
# def longest_consecutive_sequence(arr):
#     num_set = set(arr)
#     longest_streak = 0

#     for num in num_set:
#         # Check if it's the start of a sequence
#         if num - 1 not in num_set:
#             lenght = 0
#             while num+lenght in num_set:
#                 lenght+=1
#             longest_streak = max(longest_streak, lenght)

#         # if numbaer 
#     return longest_streak

# arr = [1, 9, 3, 10, 4, 20, 2]
# print(longest_consecutive_sequence(arr))  # Output: 4 (for the sequence [1, 2, 3, 4])





def longest_consecutive_sequence(arr):
    num_set = set(arr)
    longest_streak = 0
    longest_sequence = []

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_length = 0
            current_sequence = []

            # Count the length of the sequence and build the sequence
            while num + current_length in num_set:
                current_sequence.append(num + current_length)
                current_length += 1
            
            # Update longest streak and sequence if current is longer
            if current_length > longest_streak:
                longest_streak = current_length
                longest_sequence = current_sequence

    return longest_streak, longest_sequence

# arr = [11, 1, 9, 3, 10, 4, 20, 2]
arr = [1, 9, 3, 10, 4, 20, 2]
length, sequence = longest_consecutive_sequence(arr)
print(f"Length: {length}, Sequence: {sequence}")  # Output: Length: 4, Sequence: [1, 2, 3, 4]



# def longest_consecutive_sequence(arr):
#     num_set = set(arr)
#     longest_streak = 0

#     for num in num_set:
#         # Check if it's the start of a sequence
#         if num - 1 not in num_set:
#             current_num = num
#             current_streak = 1

#             # Count the length of the sequence
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_streak += 1

#             longest_streak = max(longest_streak, current_streak)

#     return longest_streak

# arr = [1, 9, 3, 10, 4, 20, 2]
# print(longest_consecutive_sequence(arr))  # Output: 4 (for the sequence [1, 2, 3, 4])
