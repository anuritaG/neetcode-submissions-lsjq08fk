class Solution:
    def jump(self, nums: List[int]) -> int:
        jmp = 0
        maxJmp = nums[0]
        ctr = 0
        for i in range(len(nums)-1):
            if i <= jmp:
                maxJmp = max(maxJmp, i+ nums[i])
            if i == jmp:
                ctr += 1
                jmp = maxJmp
                maxJmp = 0
        
        return ctr
        