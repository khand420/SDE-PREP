from itertools import combinations, permutations 

items = ['A', 'B', 'C', 'D']
print(list(combinations(items, 2)))  
  # Outputs: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]


print(list(permutations(items, 2)))  
# Outputs: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]




# my_list = [1, 2, 3, 2, 4]
# my_list.remove(3)
# print(my_list)  # Output: [1, 3, 2, 4]

