class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            if num >= 0:
                hashSet.add(num)
        # print("hash", hashSet)
        num = 1
        while num <= len(nums):
            # print("num", num)
            if num not in hashSet:
                return num
            num += 1
        return num