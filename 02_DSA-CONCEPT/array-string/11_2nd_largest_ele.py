# def find_largest(arr):
#     if not arr:
#         return None
#     largest = arr[0]
#     for num in arr:
#         if num > largest:
#             largest = num
#     return largest


def find_second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

find_second_largest([3,4,5,7,8,2])