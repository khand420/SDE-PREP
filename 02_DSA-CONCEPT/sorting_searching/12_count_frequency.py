def count(arr, x):
    # Your code goes here
    count = 0 
    for i in arr:
        if i == x:
            count+=1 
    return count        

x = 3
arr = [1, 1, 1, 2, 2, 3, 3]

print(count(arr, x))