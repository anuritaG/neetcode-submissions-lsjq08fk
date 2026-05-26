class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {}
        bracketMap[")"] = "("
        bracketMap["}"] = "{"
        bracketMap["]"] = "["
        for char in s:
            if char not in bracketMap:
                stack.append(char)
            if char in bracketMap:
                if len(stack)==0 or stack[-1] != bracketMap[char]:
                    return False
                stack.pop(-1)
        if len(stack) == 0:
            return True
        return False