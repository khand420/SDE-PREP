from collections import deque

class QueueList:
    def __init__(self):
        self.queue = []
        # self.queue = deque()

    def enqueue(self, x):
        self.queue.append(x)  # Add to end

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)  # Remove from front

    def front(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)


if __name__ == "__main__":
    print("\n=== Queue using List ===")
    q1 = QueueList()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.display()
    print("Dequeue:", q1.dequeue())
    print("Front:", q1.front())
    print("Size:", q1.size())
    q1.display()
    q1.enqueue(40)
    q1.display()
    print("Dequeue:", q1.dequeue())
    q1.display()
    print("Is Empty:", q1.isEmpty())
    print("Size:", q1.size())   