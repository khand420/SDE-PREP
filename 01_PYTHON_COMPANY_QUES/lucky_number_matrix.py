def find_lucky_numbers(matrix):
    # Find the minimum values for each row
    min_in_rows = [min(row) for row in matrix]
    
    # Find the maximum values for each column
    max_in_columns = [max(col) for col in zip(*matrix)]
    
    lucky_numbers = []
    
    # Iterate through each element to find lucky numbers
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == min_in_rows[i] and matrix[i][j] == max_in_columns[j]:
                lucky_numbers.append(matrix[i][j])
    
    return lucky_numbers

# Test the function with the given matrix
matrix = [
    [1, 10, 4, 2],
    [9, 3, 8, 7],
    [15, 16, 17, 12]
]

lucky_numbers = find_lucky_numbers(matrix)
print("Lucky Numbers:", lucky_numbers)
