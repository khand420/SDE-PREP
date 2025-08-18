class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("DoublyLinkedList  is Empty :{")
        else:
            n = self.head
            while n is not None:
                print(n.data, "->", end=" ")
                n = n.nref

    def printReversed(self):
        if self.head is None:
            print("DoublyLinkedList Reverse Order is Empty :{") 
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "->", end="")
                n = n.pref    

    def Insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")               

    def add_Begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node

    def add_After(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Liked List is Empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node




######## Delelting Node ############################
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we cant Delete nodes!")
        else:
            self.head = self.head.ref  



    def delete_end(self):
        if self.head is None:
            print("LL is empty so we cant Delete nodes!")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def deleteByValue(self, x):
        if self.head is None:
            print("LL is empty so we cant Delete nodes!")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present")            
        else:  
            n.ref = n.ref.ref
                  


DLL = DoublyLinkedList()
DLL.add_Begin(1)
DLL.add_Begin(2)
DLL.add_Begin(3)
DLL.add_Begin(4)

DLL.add_end(0)
DLL.add_end(100)


# add between into LL
# DLL.add_After(10, 3)
# DLL.add_before(5, 0)

# DLL.delete_begin()
# # DLL.delete_end()
# DLL.deleteByValue(0)
# DLL.print_LL()
DLL.printReversed()
