
def inversionCount(arr):
    
    n = len(arr) 
    invCount = 0  

    for i in range(n - 1):
        for j in range(i + 1, n):
          
            # If the current element is greater than the next,
            # increment the count
            if arr[i] > arr[j]:
                invCount += 1
            
    return invCount  

if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(inversionCount(arr))





# def merge(arr, st, mid, end):
#     # Create a temporary array
#     temp = []
#     i = st
#     j = mid + 1
#     inv_count = 0

#     while i <= mid and j <= end:
#         if arr[i] <= arr[j]:
#             temp.append(arr[i])
#             i += 1
#         else:
#             temp.append(arr[j])
#             inv_count += mid - i + 1  # increment inversion count
#             j += 1

#     while i <= mid:
#         temp.append(arr[i])
#         i += 1

#     while j <= end:
#         temp.append(arr[j])
#         j += 1

#     for i in range(st, end + 1):
#         arr[i] = temp[i - st]

#     return inv_count


# def mergeSort(arr, st, end):
#     if end <= st:
#         return 0  # return 0 inversions for single-element array

#     mid = (st + end) // 2
#     leftInverCount = mergeSort(arr, st, mid)
#     rightInverCount = mergeSort(arr, mid + 1, end)
#     inverCount = merge(arr, st, mid, end)

#     return leftInverCount + rightInverCount + inverCount


# if __name__ == "__main__":
#     # arr = [1, 20, 6, 4, 5]
#     arr = [6, 3, 5, 2, 7]

#     ans = mergeSort(arr, 0, len(arr) - 1)
#     print(ans)