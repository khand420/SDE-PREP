# def compute_gcd(a, b):
#     while b != 0:
#         a, b = b, a % b  # Update a and b
#     return a  # GCD is found when b becomes 0

# def compute_lcm(a, b):
#     gcd_value = compute_gcd(a, b)  # Calculate GCD
#     lcm_value = abs(a * b) // gcd_value  # Calculate LCM
#     return [lcm_value, gcd_value]  # Return as an array

# # # Example usage
# a = 14
# b = 8
# result = compute_lcm(a, b)
# print(result)  # Output: [10, 5]




# Examples:

# Input: a = 5 , b = 10
# Output: [10, 5]
# Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
# Input: a = 14 , b = 8
# Output: [56, 2]
# Explanation: LCM of 14 and 8 is 56, while their GCD is 2.
# Input: a = 1 , b = 1
# Output: [1, 1]
# Explanation: LCM of 1 and 1 is 1, while their GCD is 1.

def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Update a and b
    return a  # GCD is found when b becomes 0

def compute_lcm(a, b):
    gcd_value = compute_gcd(a, b)  # Calculate GCD
    return abs(a * b) // gcd_value  # Calculate LCM

def gcd_multiple(numbers):
    gcd_result = numbers[0]
    for num in numbers[1:]:
        gcd_result = compute_gcd(gcd_result, num)
    return gcd_result

def lcm_multiple(numbers):
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = compute_lcm(lcm_result, num)
    return lcm_result

# Example usage
numbers = [5, 10, 15]
gcd_result = gcd_multiple(numbers)
lcm_result = lcm_multiple(numbers)

print("GCD:", gcd_result)  # Output: GCD: 5
print("LCM:", lcm_result)  # Output: LCM: 30
