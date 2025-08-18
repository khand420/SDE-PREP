def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for token in tokens:
        if token not in ('+','-','*','/'):
            stack.append(token)
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if token=="+":
                stack.append(num2+num1)
            elif token=='-':
                stack.append(num1-num2)
            elif token=='*':
                stack.append(num1*num2)
            else:
                stack.append(num1/num2)
    return int(stack[-1])  
             



# def evalRPN(tokens):
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
    
#     return stack[0]  # The result will be the only element left in the stack

# Example usage:
tokens = ["2", "1", "+", "3", "*"]
result = evalRPN(tokens)
print(result)  # Output: 9

tokens = ["4", "13", "5", "/", "+"]
result = evalRPN(tokens)
print(result)  # Output: 6

# tokens = ["10", "6", "9", "3", "/", "-", "*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

result = evalRPN(tokens)
print(result)  # Output: -60
