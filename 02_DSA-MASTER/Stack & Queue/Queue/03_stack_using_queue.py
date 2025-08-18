from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Push x to q2
        self.q2.append(x)

        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.empty():
            return None
        return self.q1.popleft()

    def top(self):
        if self.empty():
            return None
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0






s = MyStack()
s.push(10)
s.push(20)
s.push(30)

print(s.top())   # 30
print(s.pop())   # 30
print(s.top())   # 20
print(s.empty()) # False
