import heapq

def merge_k_sorted_lists(lists):
    return list(heapq.merge(*lists))

# Example usage
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
output = merge_k_sorted_lists(lists)
print(output)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]



def merge_k_sorted_lists(lists):
    # Concatenate all lists and sort the result
    merged_list = sorted([item for sublist in lists for item in sublist])
    return merged_list

# Example usage
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
output = merge_k_sorted_lists(lists)
print(output)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]


# nlst = []
# for i in str(lists):
#     if int(i.isnumeric()):
#         nlst.append(int(i))  

# print(nlst)





# import heapq

# heapq.merge(list)
