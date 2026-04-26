class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maxIdx = 0
        # maxJmp = nums[0]
        # for idx in range(1, len(nums)):
        #     if idx > maxIdx + maxJmp:
        #         return False
        #     if maxJmp <= idx + nums[idx]:
        #         maxJmp = nums[idx]
        #         maxIdx = idx
        jmp = nums[0]
        for idx in range(1, len(nums)):
            if idx > jmp:
                return False
            jmp = max(jmp, idx + nums[idx]) 
        return True

