def encode(num):
    base62_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    while num > 0:
        code = base62_chars[num % 62] + code
        num //= 62
    return code

# Test cases
# print(encode(0))      # Should return an empty string or '0' depending on your design
# print(encode(1))      # Should return '1'
# print(encode(10))     # Should return 'a'
# print(encode(61))     # Should return 'Z'
# print(encode(62))     # Should return '10'
print(encode(12345))  # Example, should return a Base62 encoded string
# print(encode(99999))  # Example, should return a Base62 encoded string




# encode(0): Tests the function with zero. Depending on your design, you might want to handle this case specifically (e.g., returning an empty string or '0').
# encode(1): Tests the smallest non-zero input.
# encode(10): Should return 'a', as it represents the 11th character in Base62.
# encode(61): Should return 'Z', the last character before transitioning to two characters (e.g., '10').
# encode(62): Should return '10', indicating the transition to a new digit.
# encode(12345): Tests with a larger number; the expected output will depend on the encoding logic.
# encode(99999): Another larger number to test the function's performance and correctness.