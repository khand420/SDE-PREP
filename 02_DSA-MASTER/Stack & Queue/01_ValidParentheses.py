def isValid(s: str) -> bool:
    # stack = []  # Stack to store opening brackets

    # for ch in s:
    #     if ch in "({[":
    #         stack.append(ch)
    #     else:
    #         if not stack:
    #             return False
    #         if ch == ')' and stack[-1] != '(':
    #             return False
    #         if ch == '}' and stack[-1] != '{':
    #             return False
    #         if ch == ']' and stack[-1] != '[':
    #             return False
    #         stack.pop()  # Remove matched opening bracket

    # return not stack  # Stack should be empty if all matched


    # # Create a pair of opening and closing parrenthesis...
    # opcl = dict(('()', '[]', '{}'))
    # # Create stack data structure...
    # stack = []
    # # Traverse each charater in input string...
    # for idx in s:
    #     # If open parentheses are present, append it to stack...
    #     if idx in '([{':
    #         stack.append(idx)
    #     # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
    #     # If not, we need to return false...
    #     elif len(stack) == 0 or idx != opcl[stack.pop()]:
    #         return False
    # # At last, we check if the stack is empty or not...
    # # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
    # return len(stack) == 0



    d = {'(':')', '{':'}','[':']'}
    stack = []
    for i in s:
        if i in d:  # 1
            stack.append(i)
            
        # print(d[stack.pop()])
        elif len(stack) == 0 or d[stack.pop()] != i:  # 2
            return False
    return len(stack) == 0 

s = "()[]{}"

print(isValid(s))


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true