class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            if nums[idx] < 0:
                nums[idx] = 0
        
        for num in nums:
            idx = abs(num) - 1
            if idx >= len(nums) or idx<0 or nums[idx] < 0 :
                continue
            if nums[idx] == 0:
                nums[idx] = 1
            nums[idx] = -nums[idx]
        
        for i in range(1,len(nums)+1):
            if nums[i-1] >= 0:
                return i

        return len(nums)+1