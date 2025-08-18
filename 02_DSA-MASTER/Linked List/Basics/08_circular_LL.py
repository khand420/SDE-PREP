
# Insert at head
# Insert at tail
# Delete at head
# Delete at tail

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None  # We keep track of the tail for easy insertions/deletions

    def insert_head(self, data):
        new_node = Node(data)
        if not self.tail:  # Empty list
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if not self.tail:  # Empty list
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def delete_head(self):
        if not self.tail:
            print("List is empty.")
            return

        head = self.tail.next
        if self.tail == head:  # Only one node
            self.tail = None
        else:
            self.tail.next = head.next

    def delete_tail(self):
        if not self.tail:
            print("List is empty.")
            return

        head = self.tail.next
        if self.tail == head:  # Only one node
            self.tail = None
        else:
            temp = head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.tail.next
            self.tail = temp

    def display(self):
        if not self.tail:
            print("List is empty.")
            return

        current = self.tail.next
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.tail.next:
                break
        print("(back to head)")




cll = CircularLinkedList()
cll.insert_head(10)
cll.insert_tail(20)
cll.insert_head(5)
cll.display()  # Output: 5 -> 10 -> 20 -> (back to head)

cll.delete_head()
cll.display()  # Output: 10 -> 20 -> (back to head)

cll.delete_tail()
cll.display()  # Output: 10 -> (back to head)
