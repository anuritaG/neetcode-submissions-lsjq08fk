class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '{', '[']
        # close_brackets = []
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                popped_bracket = stack[-1]
                if bracket == ')' and popped_bracket != '(':
                    return False
                if bracket == '}' and popped_bracket != '{':
                    return False
                if bracket == ']' and popped_bracket != '[':
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True