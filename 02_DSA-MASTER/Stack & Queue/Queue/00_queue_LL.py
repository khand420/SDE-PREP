class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0

    def enqueue(self, x):
        new_node = Node(x)
        if self.rear_node:
            self.rear_node.next = new_node
        self.rear_node = new_node

        if not self.front_node:
            self.front_node = new_node

        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        result = self.front_node.data
        self.front_node = self.front_node.next
        if not self.front_node:
            self.rear_node = None
        self.count -= 1
        return result

    def front(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front_node.data

    def isEmpty(self):
        return self.front_node is None

    def size(self):
        return self.count

    def display(self):
        curr = self.front_node
        q = []
        while curr:
            q.append(curr.data)
            curr = curr.next
        print("Queue:", q)


if __name__ == "__main__":
    print("\n=== Queue using Linked List ===")
    q2 = QueueLinkedList()
    q2.enqueue(100)
    q2.enqueue(200)
    q2.enqueue(300)
    q2.display()
    print("Dequeue:", q2.dequeue())
    print("Front:", q2.front())
    print("Size:", q2.size())
    q2.display()
    q2.enqueue(400)
    q2.display()
    print("Dequeue:", q2.dequeue())
    q2.display()
    print("Is Empty:", q2.isEmpty())
    print("Size:", q2.size())   