class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx in range(len(temperatures)):
            # stack.append(temp)
            while len(stack) > 0 and stack[-1][0] < temperatures[idx]:
                result[stack[-1][1]] = idx - stack[-1][1] 
                stack.pop(-1)
            stack.append((temperatures[idx], idx))
        return result
                