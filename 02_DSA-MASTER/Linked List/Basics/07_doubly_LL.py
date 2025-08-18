class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, data):
        new_node = Node(data)
        if not self.head:  # Empty list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_back(self, data):
        new_node = Node(data)
        if not self.tail:  # Empty list
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if not self.head:  # Empty list
            print("List is empty")
            return None
        data = self.head.data
        if self.head == self.tail:  # Only one element
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def pop_back(self):
        if not self.tail:  # Empty list
            print("List is empty")
            return None
        data = self.tail.data
        if self.head == self.tail:  # Only one element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")

# Example usage:
dll = DoublyLinkedList()
dll.add_front(10)
dll.add_back(20)
dll.add_front(5)
dll.display()  # Output: 5 <-> 10 <-> 20 <-> None

dll.pop_front()
dll.display()  # Output: 10 <-> 20 <-> None

dll.pop_back()
dll.display()  # Output: 10 <-> None
