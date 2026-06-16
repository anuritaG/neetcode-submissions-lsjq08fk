class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # At every level, we have 2 choice: either to add current number 
        # in subset or not consider it
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            dfs(i+1)
            subset.append(nums[i])
            dfs(i+1)
            # need to remove current choice as it is already present in subset
            subset.pop()
        dfs(0)
        return res