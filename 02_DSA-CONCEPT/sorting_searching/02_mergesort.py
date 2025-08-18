def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2 
        leftlst = lst[mid:]
        rightlst = lst[:mid]

        mergeSort(leftlst)
        mergeSort(leftlst)

        i=j=k=0

        while i < len(leftlst) and j < len(rightlst):
            if leftlst[i] < rightlst[j]:
                lst[k] = leftlst[i]
                i+=1
            else:
                lst[k] = rightlst[j]   
                j+=1
            k+=1

        while i < len(leftlst):
            lst[k] = leftlst[i]
            i+=1  
            k+=1   

        while j < len(rightlst):
            lst[k] = rightlst[j]    
            j+=1
            k+=1           

lst = [2,5,4,1,0,0]
mergeSort(lst)
print(lst)


