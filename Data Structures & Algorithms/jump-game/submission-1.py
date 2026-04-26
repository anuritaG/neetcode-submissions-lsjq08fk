class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # at any point i: jmp = max Indx that can be reached by all numbers till i
        # if the max idx reached < i: there is no way anyone can reach i
        jmp = nums[0]
        for idx in range(1, len(nums)):
            if idx > jmp:
                return False
            jmp = max(jmp, idx + nums[idx]) 
        return True

