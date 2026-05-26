class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        countMap = {}
        for num in nums:
            if num > 0 and num not in countMap:
                countMap[num] = 1
        result = 1
        while(True):
            if result not in countMap:
                return result
            result += 1
        return 0