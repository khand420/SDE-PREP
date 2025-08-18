def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    # Create left and right subarrays
    left_sub = arr[left:mid + 1]
    right_sub = arr[mid + 1:right + 1]

    left_index, right_index = 0, 0
    sorted_index = left

    while left_index < len(left_sub) and right_index < len(right_sub):
        if left_sub[left_index] <= right_sub[right_index]:
            arr[sorted_index] = left_sub[left_index]
            left_index += 1
        else:
            arr[sorted_index] = right_sub[right_index]
            right_index += 1
        sorted_index += 1

    while left_index < len(left_sub):
        arr[sorted_index] = left_sub[left_index]
        left_index += 1
        sorted_index += 1

    while right_index < len(right_sub):
        arr[sorted_index] = right_sub[right_index]
        right_index += 1
        sorted_index += 1



def timSort(arr):
    min_run = 32
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertionSort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

# Example usage
num = [64, 34, 25, 12, 22, 11, 90]
timSort(num)
print("Sorted array (Timsort):", num)
