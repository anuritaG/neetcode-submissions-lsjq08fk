class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(0, len(res)):
                item = res[j]
                res.append(item+[nums[i]])
        return res