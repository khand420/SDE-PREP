def BubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:

                lst[j] , lst[j+1] = lst[j+1] , lst[j]
lst = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(lst)
print("Sorted array:", lst)