def is_balanced(exp):
    # Dictionary to hold matching pairs of brackets
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # Stack to hold opening brackets
    stack = []
    
    # Traverse each character in the expression
    for char in exp:
        # If it's an opening bracket, push it onto the stack
        if char in matching_bracket.values():
            stack.append(char)
        # If it's a closing bracket, check if it matches the top of the stack
        elif char in matching_bracket.keys():
            # Check if the stack is not empty and top of the stack matches the corresponding opening bracket
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()  # Pop the top of the stack since we have a match
            else:
                return False  # If no match, the expression is not balanced
        else:
            continue  # Ignore other characters

    # If the stack is empty at the end, the expression is balanced
    return not stack


# Test the function with an example input
exp = "[()]{}{[()()]()}"
if is_balanced(exp):
    print("Balanced")
else:
    print("Not Balanced")





def is_balanced(exp):
    # Stack to keep track of opening brackets
    stack = []

    # Dictionary to match opening and closing brackets
    brackets = {'(': ')', '{': '}', '[': ']'}

    # Traverse each character in the expression
    for char in exp:
        # If the character is an opening bracket, push it onto the stack
        if char in brackets:
            stack.append(char)
        # If the character is a closing bracket
        elif char in brackets.values():
            # Check if the stack is empty or the top of the stack doesn't match the current closing bracket
            if not stack or brackets[stack.pop()] != char:
                return False

    # If the stack is empty, the expression is balanced
    return not stack


# Test the function with an example input
exp = "[()]{}{[()()]()}"
if is_balanced(exp):
    print("Balanced")
else:
    print("Not Balanced")
