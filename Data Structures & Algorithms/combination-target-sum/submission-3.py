class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def recur(i, add, subset):
            # print("entered", subset, "res", res)
            if add < 0 or i >= len(nums):
                # print("returned")
                return 
            if add == 0:
                # print("entered 0")
                res.append(subset.copy())
                # print("res", res)
                return 
            subset.append(nums[i])
            # print("subset after append", subset)
            recur(i, add-nums[i], subset)
            subset.remove(nums[i])
            recur(i+1, add, subset)
        recur(0, target, subset)
        return res
