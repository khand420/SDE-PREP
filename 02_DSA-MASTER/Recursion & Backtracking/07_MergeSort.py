# def MergeSort(arr):

#     # Deviding into subArray

#     if len(arr) > 1:
#         mid = len(arr)//2
#         left_arr = arr[mid:]
#         right_arr = arr[:mid]
#         MergeSort(left_arr)
#         MergeSort(right_arr)

#         i = 0
#         j = 0 
#         k = 0

#         # Merging sub-Array
#         while i<len(left_arr) and j<len(right_arr):
#             if left_arr[i] < right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i = i+1
#                 k = k+1
#             else:
#                 arr[k] = right_arr[j] 
#                 j = j+1  
#                 k = k+1  
        
#         # checking any subArray Left
#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i = i+1
#             k = k+1

#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j = j+1
#             k = k+1    


# arr = [5,7,1,5,0,8]

# MergeSort(arr)
# print(arr)






def merge(arr, st, mid, end):
    # Create a temporary array
    temp = []
    i = st
    j = mid + 1

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j += 1

    for i in range(st, end + 1):
        arr[i] = temp[i - st]


def mergeSort(arr, st, end):
    if end > st:
        mid = (st + end) // 2
        mergeSort(arr, st, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, st, mid, end)

    return arr


if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    ans = mergeSort(arr, 0, len(arr) - 1)
    print(ans)