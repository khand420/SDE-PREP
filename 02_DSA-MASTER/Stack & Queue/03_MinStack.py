# class MinStack(object):

#     def __init__(self):
#         self.minStack = []
#         self.stack = []

        

#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         self.stack.append(val)
#         if self.minStack:
#             val = min(val, self.minStack[-1])
#         self.minStack.append(val)

        

#     def pop(self):
#         """
#         :rtype: None
#         """
#         self.minStack.pop()
#         self.stack.pop()
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]
        

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.minStack[-1]
        


# # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(4)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Stack to store the minimums

    def push(self, x: int) -> None:
        self.stack.append(x)
        # If min_stack is empty or the new element is smaller or equal to the current minimum
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
            # If the popped element is the minimum, pop it from the min_stack as well
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Returns -3
min_stack.pop()
print(min_stack.top())      # Returns 0
print(min_stack.getMin())   # Returns -2
