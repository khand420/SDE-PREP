class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "->", end=" ")
                n = n.ref

    def add_Begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

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

    def Insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")


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

    def reverse(self):
        privious = None
        while self.head:
            temp = self.head
            self.head = self.head.ref
            temp.ref = privious
            privious = temp
        return privious        
                        


LL1 = LinkedList()
LL1.add_Begin(1)
LL1.add_Begin(2)
LL1.add_Begin(3)
LL1.add_Begin(4)

LL1.add_end(0)
LL1.add_end(100)

# add between into LL
LL1.add_After(10, 3)
LL1.add_before(5, 0)

LL1.delete_begin()
# LL1.delete_end()
LL1.deleteByValue(0)

LL1.print_LL()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.start = None

#     def Traversal (self):
#         if self.start == None:
#             print("List is Empty!")
#         else:
#             temp = self.start
#             while temp != None:
#                print(temp.data, end=' ')
#                temp = temp.next


#     def DeleteFirt(self):
#         if self.start == None:
#             print("List is Empty!")
#         else:
#             self.start = self.start.next


#     def InsertAtEnd(self, value):
#         newNode = Node(value)

#         if self.start == None:
#             self.start = newNode
#         else:
#             last = self.start
#             while last.next != None:
#                 last = last.next
#             last.next = newNode


# mylist = LinkedList()

# mylist.InsertAtEnd(2)
# mylist.InsertAtEnd(5)
# mylist.InsertAtEnd(23)
# mylist.InsertAtEnd(24)
# mylist.InsertAtEnd(0)
# mylist.InsertAtEnd(7)


# mylist.Traversal()
# print()

# mylist.DeleteFirt()

# mylist.Traversal()


# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next

#         return count

#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return

#         itr = self.head

#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data, None)

#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.insert_at_begining(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break

#             itr = itr.next
#             count += 1

#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break

#             itr = itr.next
#             count+=1

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)


# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.insert_at(1,"blueberry")
#     ll.remove_at(2)
#     ll.print()

#     ll.insert_values([45,7,12,567,99])
#     ll.insert_at_end(67)
#     ll.print()
