class MyQueue(object):

    def __init__(self):
        self.stack1 = []  # Main stack (acts like queue)
        self.stack2 = []  # Temporary stack

    def push(self, x):
        # Move all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # Push the new element into stack1
        self.stack1.append(x)

        # Push everything back to stack1 from stack2
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        if self.empty():
            return None
        return self.stack1.pop()  # Pop from front of queue

    def peek(self):
        if self.empty():
            return None
        return self.stack1[-1]  # Peek at front of queue

    def empty(self):
        return len(self.stack1) == 0


q = MyQueue()
q.push(10)
q.push(20)
q.push(30)

print(q.peek())  # 10
print(q.pop())   # 10
print(q.peek())  # 20
print(q.empty()) # False
