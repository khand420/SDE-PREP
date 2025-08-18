def isSorted(arr, n):

    if n == 0 or n == 1:
        return True
    
    return arr[n-1] >= arr[n-2] and isSorted(arr, n-1)





arr = [1,2,3,4,]
n = len(arr)

print(isSorted(arr, n))