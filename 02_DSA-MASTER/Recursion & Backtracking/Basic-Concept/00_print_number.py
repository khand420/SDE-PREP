# anything that can be solved using a for loop can also be solved with recursion.


def printNumber(n):
    if n == 0:          
        return
    # print(n) 
    printNumber(n - 1)  
    print(n)             

printNumber(5)
