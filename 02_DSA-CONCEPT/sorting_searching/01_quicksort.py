def quickSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        lesser = [x for x in lst[1:] if x <= pivot]
        greater = [x for x in lst[1:] if x >= pivot]
        return quickSort(lesser)+[pivot]+quickSort(greater)
    
lst = [3,4,2,1,7,0,0]
newlst = quickSort(lst)

print(newlst)
