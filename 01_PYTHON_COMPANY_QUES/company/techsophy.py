def MultiplicativePersistence(num):
    if num < 10:
        return 0  # If num is a single digit, return 0
    
    count = 0
    while num >= 10:  # Continue until num is a single digit
        product = 1
        for digit in str(num):  # Multiply the digits
            product *= int(digit)
        num = product  # Update num to the product of its digits
        count += 1  # Increment the count of multiplications
    
    return count

# Test cases
print(MultiplicativePersistence(4))   # Output: 0
print(MultiplicativePersistence(25))  # Output: 2
print(MultiplicativePersistence(39))  # Output: 3



