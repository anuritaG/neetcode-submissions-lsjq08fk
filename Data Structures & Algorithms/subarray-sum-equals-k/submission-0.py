class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = {}
        prefixMap[0] = 1
        prefixSum = 0
        result = 0
        for num in nums:
            prefixSum += num
            diff = prefixSum - k
            if diff in prefixMap:
                result += prefixMap[diff]
            if prefixSum not in prefixMap:
                prefixMap[prefixSum] = 0
            prefixMap[prefixSum] += 1
        return result