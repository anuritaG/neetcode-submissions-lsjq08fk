class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first_ptr = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[first_ptr] = nums[index]
                first_ptr += 1
        return first_ptr
        
            