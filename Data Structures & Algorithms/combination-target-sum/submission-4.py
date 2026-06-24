class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def recur(i, add, subset):
            if add < 0 or i >= len(nums):
                return 
            if add == 0:
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            recur(i, add-nums[i], subset)
            subset.remove(nums[i])
            recur(i+1, add, subset)
        recur(0, target, subset)
        return res
