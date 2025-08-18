

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top
        self.top = self.top.next
        self._size -= 1
        return popped.value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def __str__(self):
        result = []
        current = self.top
        while current:
            result.append(current.value)
            current = current.next
        return str(result)
if __name__ == "__main__":

    print("\n=== Stack using Linked List ===")
    s2 = StackLinkedList()
    s2.push(100)
    s2.push(200)
    s2.push(300)
    print("Stack:", s2)
    print("Pop:", s2.pop())
    print("Peek:", s2.peek())
    print("Size:", s2.size())





#  Steps
# Create a Node class with value and next

# Stack class holds:

# self.top → points to top node

# self._size → tracks number of elements

# Push:

# Create new node

# Point new_node.next = top

# Set top = new_node

# Pop:

# Save current top

# Move top = top.next

# Return saved value

# Peek: Return top.value

# Empty / Size: Use conditions and _size