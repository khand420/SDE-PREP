
from collections import deque 

class StackList:
    def __init__(self):
        # self.stack = []
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    print("=== Stack using List ===")
    s1 = StackList()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    print("Stack:", s1)
    print("Pop:", s1.pop())
    print("Peek:", s1.peek())
    print("Size:", s1.size())