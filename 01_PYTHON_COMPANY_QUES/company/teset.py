# Complete the 'create_paginator' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY items
#  2. INTEGER pageSize
#
# The function must act as a generator
# 

# def create_paginator(items: list, pageSize: int) -> list:
    
#     arr = []
#     # str =  ''
#     for i in range(0, len(items)+1, pageSize):
#         print(items[i:pageSize])
        
    
#     print('arr--', items[0:pageSize])
    
    # print('items--', items, pageSize)
    

def create_paginator(items: list, pageSize: int) -> list:
    arr = []
    for i in range(0, len(items), pageSize):
        arr.append(items[i:i + pageSize])
    return arr
    # return list(map(lambda x: items[x:x+pageSize], range(0, len(items), pageSize)))
    return [items[i:i+pageSize] for i in range(0, len(items), pageSize)]
# Example usage:
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pageSize = 3
paginator = create_paginator(items, pageSize)
print(paginator)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



#  \
#  Enter your query below.
# Please append a semicolon ";" at the end of the query
# */

# SELECT protocol, traffic_in, traffic_out 
# FROM traffic WHERE traffic_in > traffic_out;         