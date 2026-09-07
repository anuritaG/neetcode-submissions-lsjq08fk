class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        res = 0
        for num in nums:
            if (num-1) in hashSet:
                continue
            count = 1
            nextNum = num + 1
            
            while nextNum in hashSet:
                count += 1
                nextNum += 1
            res = max(count, res)
        return res
