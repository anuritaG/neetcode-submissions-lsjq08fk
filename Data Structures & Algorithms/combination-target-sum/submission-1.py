class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 2 branches: 1 take the current value, 2: do not take the current value
        res = []
        subset = []
        def dfs(i, amt):
            if amt == 0:
                res.append(subset.copy())
                return
            if amt < 0 or i >= len(nums):
                return
            subset.append(nums[i])
            dfs(i, amt-nums[i])
            subset.pop()
            dfs(i+1, amt)
        dfs(0, target)
        return res