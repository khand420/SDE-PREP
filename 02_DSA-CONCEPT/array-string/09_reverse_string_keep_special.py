def reverse_string_keep_special(s):
    # Create a list of characters from the string
    chars = [c for c in s if c.isalnum()]
    result = []

    # Reverse the list of alphanumeric characters
    chars.reverse()
    char_index = 0

    for c in s:
        if c.isalnum():
            result.append(chars[char_index])
            char_index += 1
        else:
            result.append(c)

    return ''.join(result)

   
        

# Example usage
input_string = "a,b$cow"
reversed_string = reverse_string_keep_special(input_string)

print(reversed_string)  # Output: "c,b$a"






# def reverse_string_keep_special(s):
#     # Convert the string to a list for mutability
#     s_list = list(s)
    
#     # Initialize pointers
#     left, right = 0, len(s_list) - 1
    
#     while left < right:
#         # Move left pointer to the next valid character
#         while left < right and not s_list[left].isalnum():
#             left += 1
#         # Move right pointer to the previous valid character
#         while left < right and not s_list[right].isalnum():
#             right -= 1
        
#         # Swap valid characters
#         s_list[left], s_list[right] = s_list[right], s_list[left]
        
#         # Move both pointers
#         left += 1
#         right -= 1
    
#     # Join the list back into a string
#     return ''.join(s_list)

# # Example usage
# input_string = "a,b$c"
# reversed_string = reverse_string_keep_special(input_string)

# print(reversed_string)  # Output: "c,b$a"
