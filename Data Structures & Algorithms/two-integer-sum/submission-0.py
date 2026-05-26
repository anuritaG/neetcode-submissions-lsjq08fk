class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        extras = {}
        for i in range(len(nums)):
            if nums[i] in extras:
                return [extras[nums[i]], i]
            extras[target - nums[i]] = i
        return [-1, -1]