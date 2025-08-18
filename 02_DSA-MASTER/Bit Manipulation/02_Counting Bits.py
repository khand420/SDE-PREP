def countingBits(num):
    # one_bits_counter = [0]*(num+1)

    # for i in range(num+1):
    #     one_bits_counter[i] = one_bits_counter[i//2]+ i%2
    # return one_bits_counter

    return [bin(i).count('1') for i in range(num+1)]

n = 5
print(countingBits(n))


    


# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105