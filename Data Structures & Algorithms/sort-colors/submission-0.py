class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for i in range(3):
            for idx in range(0, len(nums)):
                if nums[idx] == i:
                    temp = nums[ptr]
                    nums[ptr] = nums[idx]
                    nums[idx] = temp
                    ptr += 1
                idx += 1
        
        