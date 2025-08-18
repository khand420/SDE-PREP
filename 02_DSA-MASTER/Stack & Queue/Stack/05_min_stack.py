class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]



s = MinStack()
s.push(5)
s.push(3)
s.push(7)

print(s.getMin())  # ➜ 3
s.pop()
print(s.top())     # ➜ 3
print(s.getMin())  # ➜ 3
s.pop()
print(s.getMin())  # ➜ 5



# | `stack`     | `min_stack` |
# | ----------- | ----------- |
# | `[5, 3, 7]` | `[5, 3, 3]` |






# class MinStack(object):

#     def __init__(self):
#         self.stack = []

#     def push(self, val):
#         if self.stack:
#             current_min = self.stack[-1][1]
#             self.stack.append((val, min(val, current_min)))
#         else:
#             self.stack.append((val, val))

#     def pop(self):
#         if self.stack:
#             self.stack.pop()

#     def top(self):
#         if self.stack:
#             return self.stack[-1][0]

#     def getMin(self):
#         if self.stack:
#             return self.stack[-1][1]



# | Operation | Stack Content                | Top Value | Current Min |
# | --------- | ---------------------------- | --------- | ----------- |
# | `push(5)` | `[ (5, 5) ]`                 | `5`       | `5`         |
# | `push(3)` | `[ (5, 5), (3, 3) ]`         | `3`       | `3`         |
# | `push(7)` | `[ (5, 5), (3, 3), (7, 3) ]` | `7`       | `3`         |
