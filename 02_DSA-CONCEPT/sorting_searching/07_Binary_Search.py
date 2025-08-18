def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the mid index
        
        # Check if the target is present at mid
        if arr[mid] == target:
            return mid  # Target found
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
            
    return -1  # Target not found

# Example usage
sorted_array = [11, 12, 22, 25, 34, 64, 90]
target = 25
result = binary_search(sorted_array, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
