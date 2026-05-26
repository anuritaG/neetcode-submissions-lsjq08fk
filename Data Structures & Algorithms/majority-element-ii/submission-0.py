class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequencyMap = {}
        for num in nums:
            if num not in frequencyMap:
                frequencyMap[num] = 0
            frequencyMap[num] += 1
        threshold = len(nums) / 3
        result = []
        for num in frequencyMap:
            if frequencyMap[num] > threshold:
                result.append(num)
        return result