class Solution:
    def jump(self, nums: List[int]) -> int:
        jmp = 0
        maxJmp = nums[0]
        ctr = 0
        # trick: do not iterate for the last element as reaching the last element is goal
        # which is guarenteed
        for i in range(len(nums)-1):
            # Find the max. till jump allowed
            if i <= jmp:
                maxJmp = max(maxJmp, i+ nums[i])
            # when reached the max. jump allowed --> next choice should be the
            # max steps covered.
            if i == jmp:
                ctr += 1
                jmp = maxJmp
                maxJmp = 0
        
        return ctr
        