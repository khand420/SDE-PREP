def leftRotate(arr, d):

    start = arr[d:]
    print(start)
    end = arr[:d]
    print(end)
    arr[:] = start+end
    return arr

    # or
        # for i in range(0,d):
        # arr.append(arr.pop(0))
    # or
    
    # arr[:]


arr = [1, 3, 4, 2]
d = 1
print(leftRotate(arr, d))
# Output: [2, 1, 3, 4]