

stack = []

def push():
    element = input("Enter the element into stack:")
    stack.append(element)
    print(stack)

#LIFO

def pop():
    if not stack:
        print("Stack is Empty !")  
    else:
        e = stack.pop()
        print("Remove Element:", e)    
        print(stack)

while True:
    print("Select the operation 1.push 2.pop 3.quit")  
    choice = int(input())

    if choice == 1:
        push()
    elif choice == 2:
       pop()    
    elif choice == 3:
       break
    else:
        print("Enter the correct operation!")