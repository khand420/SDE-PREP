def twosum(arr, n, sum):

    d = {}
    for i in range(n):
        temp = sum-arr[i]
        # if temp in d.values():
        if temp in d:

            print('Element found', arr[i], temp)
            # return
        else:
            d[arr[i]] = i
            # d[i] = arr[i]

    print(d)


# arr = [1, 4, 45, 6, 10, 8]
# sum = 16

arr= [1, 5, 7, -1, 5]
sum = 6
print(twosum(arr, len(arr), sum))


