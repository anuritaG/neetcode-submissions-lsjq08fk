class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        operands = ['+', '-', '*', '/']
        for token in tokens:
            if token in operands:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    c = a + b
                elif token == '-':
                    c = a - b
                elif token == '*':
                    c = a * b
                else:
                    c = int(a / b)
                stack.append(str(c))

            else:
                stack.append(token)
        return int(stack[-1])
