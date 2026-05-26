class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        result = 0
        for num in nums:
            curNum = num
            maxLength = 0
            if curNum-1 in hashSet:
                continue
            while curNum in hashSet:
                maxLength += 1
                # hashSet.remove(curNum)
                curNum += 1
            result = max(result, maxLength)
        return result