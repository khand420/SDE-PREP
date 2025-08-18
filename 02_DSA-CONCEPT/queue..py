#FIFO
queue = []

def Enqueue():
    element = int(input("Enter the element to Enqueue: "))
    queue.append(element)
    print(queue)

def Dequeue():
    if not queue:
        print("Queue is Empty!")
    else:
        pop = queue.pop(0)
        print("removed element:",pop)
        print(queue)


def show():
    print(queue)

while True:
    print("Select the operation 1.add 2.romove 3.show 4.quit")
    choice = int(input())

    if choice == 1:
        Enqueue()
    elif choice == 2:
        Dequeue() 
    elif choice == 3:
        show()       
    elif choice == 4:
        break
    else:
        print("Enter the correct operation")