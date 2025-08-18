def evalRPN(tokens):
#     stack = []
    
#     for token in tokens:
#         if token in ["+", "-", "*", "/"]:
#             b = stack.pop()  # Second operand
#             a = stack.pop()  # First operand
            
#             if token == "+":
#                 stack.append(a + b)
#             elif token == "-":
#                 stack.append(a - b)
#             elif token == "*":
#                 stack.append(a * b)
#             elif token == "/":
#                 # Use int() to truncate towards zero
#                 stack.append(int(a / b))
#         else:
#             stack.append(int(token))  # Push the number onto the stack
    
#     return stack[0]