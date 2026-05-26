class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        countMap = {}
        for num in nums:
            if num > 0 and num not in countMap:
                countMap[num] = 1
        for result in range(1, len(nums) + 2):
            if result not in countMap:
                return result
        return 1