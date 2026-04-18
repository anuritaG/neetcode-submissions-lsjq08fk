class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        idx_stack = []
        for idx in range(len(temperatures)):
            print(temperatures[idx])
            print(idx_stack)
            # if len(idx_stack) == 0 or temperatures[idx] <= idx_stack[-1]:
            #     idx_stack.append(idx)
            # else:
            while len(idx_stack)>0 and temperatures[idx_stack[-1]] < temperatures[idx]:
                pop_idx = idx_stack.pop()
                res[pop_idx] = idx-pop_idx
            idx_stack.append(idx)
        return res        