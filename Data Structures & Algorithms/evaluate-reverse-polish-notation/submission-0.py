class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+", "-","*", "/"]
        for char in tokens:
            print(stack)
            if char in operator:
                print(char)
                num2 = int(stack.pop(-1))
                num1 = int(stack.pop(-1))
                if char == "+":
                    print("here")
                    value = num1 + num2
                    print("value",value)
                elif char == "-":
                    value = num1 - num2
                elif char == "*":
                    value = num1 * num2
                else:
                    value = num1 / num2
                stack.append(value)
            else:
                stack.append(char) 
        return int(stack[0])
