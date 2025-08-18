def BSR(arr, target, start, end):


    while start <= end:
        mid = start+(end - start) // 2

        if arr[mid] == target:
            return True
        if target > arr[mid]:
            return BSR(arr, target, mid+1, end)
        else:
            return BSR(arr, target, start, mid-1)
            
    return False

arr = [1,3,4,5,6,7,9]
start  = 0
end = len(arr) -1
target = 6
print(BSR(arr, target, start, end))



# Time Complexity: O(log N)
# Auxiliary Space: O(1)


# def BS(arr, target):
#     start  = 0
#     end = len(arr) -1

#     while start <= end:
#         mid = start+(end - start) // 2

#         if arr[mid] == target:
#             return True
#         if target > arr[mid]:
#             start = mid+1
#         else:
#             end = mid -1 
            
#     return False


# arr = [1,3,4,5,6,7,9]
# n = len(arr)
# target = 6
# print(BS(arr, target))
