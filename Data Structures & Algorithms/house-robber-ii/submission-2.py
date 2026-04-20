class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp1 = [0] * (n)
        dp2 = [0] * (n+1)
        dp1[0] = 0
        dp1[1] = nums[0]
        dp2[0] = 0
        dp2[1] = 0
        # At a particular house i, thief has 2 options:
        # 1. Rob house i and house (i-2) 
        # 2. Rob house i-1 and leave i
        # At any house, choose max of 2 options
        for i in range(2, (n)):
            # print(i, " ", nums[i-1], " ",dp2[i-2], " ", dp2[i-1])
            dp1[i] = max((nums[i-1] + dp1[i-2]), dp1[i-1])
        for i in range(2, (n+1)):
        #     print(i, " ", nums[i-1], " ",dp2[i-2], " ", dp2[i-1])
            dp2[i] = max((nums[i-1] + dp2[i-2]), dp2[i-1]) 
        # print(dp1)
        # print(dp2)     
        return max(dp1[-1], dp2[-1])