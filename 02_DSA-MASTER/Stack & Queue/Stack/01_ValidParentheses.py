class Solution(object):
    def isValid(self, s):
        stack = []

        for i in s:
            if i in ['(', '{', '[']:  # check opening
                stack.append(i)
            else:  # check closing
                if len(stack) == 0:
                    return False
                if (stack[-1] == '(' and i == ')') or \
                   (stack[-1] == '[' and i == ']') or \
                   (stack[-1] == '{' and i == '}'):
                    stack.pop()
                else:  # no match
                    return False

        return len(stack) == 0 



# class Solution(object):
#     def isValid(self, s):
#         stack = []
#         mapping = {')': '(', ']': '[', '}': '{'}

#         for char in s:
#             if char in mapping.values():  # opening brackets
#                 stack.append(char)
#             else:  # closing brackets
#                 if not stack or stack[-1] != mapping[char]:
#                     return False
#                 stack.pop()

#         return len(stack) == 0


s = "()[]{}"

print(Solution().isValid("()"))        # True
print(Solution().isValid("({[]})"))    # True
print(Solution().isValid("([)]"))      # False
print(Solution().isValid("{[]}"))      # True
