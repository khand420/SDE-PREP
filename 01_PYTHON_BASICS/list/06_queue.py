class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop() if self.outbox else None

# Example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1