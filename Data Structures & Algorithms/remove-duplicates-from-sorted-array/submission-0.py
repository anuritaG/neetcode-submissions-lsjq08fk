class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fPtr, sPtr = 0, 1
        while sPtr < len(nums):
            curNum = nums[fPtr]
            while sPtr < len(nums) and curNum == nums[sPtr]:
                sPtr += 1
            if sPtr >= len(nums):
                return fPtr + 1
            nums[fPtr+1] = nums[sPtr]
            sPtr += 1
            fPtr += 1
        return fPtr + 1

        