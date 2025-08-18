def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a DP table to store results of subproblems
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from str1
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters to str1 to form str2

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1) # Substitution

    # The answer is in the bottom-right cell
    return dp[m][n]

# Example usage
str1 = "kitten"
str2 = "sitting"

distance = edit_distance(str1, str2)
print(f"The edit distance between '{str1}' and '{str2}' is: {distance}")
