
# def printSubsetTrace(arr, ans, i, indent=0):
#     print('  ' * indent + f"i={i}, ans={ans}")
    
#     if i == len(arr):
#         return
    
#     # Include arr[i]
#     ans.append(arr[i])
#     printSubsetTrace(arr, ans, i + 1, indent + 1)
    
#     # Backtrack
#     ans.pop()

#     # Exclude arr[i]
#     printSubsetTrace(arr, ans, i + 1, indent + 1)

# arr = [1, 2, 3]
# printSubsetTrace(arr, [], 0)





def printSubset(arr, ans, i, result):
    if i == len(arr):
        result.append(ans[:])
        return 
    
    # include arr[i]
    ans.append(arr[i])
    printSubset(arr, ans, i+1, result)

    ans.pop() #backtrack
    #exclude arr[i]
    printSubset(arr, ans, i+1, result)
    

arr = [1,2,3]
ans = []
i = 0
result = []

printSubset(arr, ans, i, result)
print(result)



