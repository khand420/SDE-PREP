def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test cases
print(singleNumber([2, 2, 1]))  # Output: 1
print(singleNumber([4, 1, 2, 1, 2]))  # Output: 4



test_cases = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
    ([0, 1, 0, 2, 1], 2),
    ([3, 3, 7, 7, 10, 10, 8], 8)
]

# Run test cases and print results
for nums, expected in test_cases:
    result = singleNumber(nums)
    print(f"Input: {nums} | Expected: {expected} | Result: {result}")
    assert result == expected  # This will raise an error if the result is not as expected




# Certainly! Let's explain how the XOR operation works in the context of the "Single Number" problem step by step. The XOR (exclusive OR) operation has some unique properties that make it particularly useful for this problem:

# ### Properties of XOR
# 1. **Self-Canceling**: \(a \oplus a = 0\) (any number XORed with itself results in 0).
# 2. **Identity**: \(a \oplus 0 = a\) (any number XORed with 0 is the number itself).
# 3. **Commutative**: \(a \oplus b = b \oplus a\) (the order of operations does not matter).
# 4. **Associative**: \((a \oplus b) \oplus c = a \oplus (b \oplus c)\) (grouping does not matter).

# ### How XOR Solves the Problem
# In the "Single Number" problem, every number except one appears twice. By applying XOR to all the numbers, the duplicates will cancel each other out, leaving only the unique number.

# ### Step-by-Step Example
# Let’s take an example array: `[4, 1, 2, 1, 2]`.

# 1. **Initialization**: Start with a variable `result` initialized to 0.
#    ```python
#    result = 0
#    ```

# 2. **XOR Operation Step-by-Step**:
#    - **Step 1**: XOR with 4
#      \[
#      result = 0 \oplus 4 = 4
#      \]
#    - **Step 2**: XOR with 1
#      \[
#      result = 4 \oplus 1 = 5 \quad \text{(binary: 100 \oplus 001 = 101)}
#      \]
#    - **Step 3**: XOR with 2
#      \[
#      result = 5 \oplus 2 = 7 \quad \text{(binary: 101 \oplus 010 = 111)}
#      \]
#    - **Step 4**: XOR with 1 (the second occurrence)
#      \[
#      result = 7 \oplus 1 = 6 \quad \text{(binary: 111 \oplus 001 = 110)}
#      \]
#    - **Step 5**: XOR with 2 (the second occurrence)
#      \[
#      result = 6 \oplus 2 = 4 \quad \text{(binary: 110 \oplus 010 = 100)}
#      \]

# 3. **Final Result**: After processing all elements, the final value of `result` is 4, which is the number that appears only once.

# ### Summary of Each Step
# - The first number (4) is stored in `result`.
# - The subsequent numbers (1, 2) modify `result` but do not affect it negatively because the duplicates (1 and 2) will cancel each other out.
# - The final result after all XOR operations will be the single number.

# ### Conclusion
# The XOR operation efficiently finds the unique number in an array where every other number appears twice. This method runs in O(n) time complexity and O(1) space complexity, making it optimal for this problem.

# If you have any more questions or need further clarification, feel free to ask!