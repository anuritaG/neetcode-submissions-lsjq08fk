class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, (n+1)):
            # At a particular house i, thief has 2 options:
            # 1. Rob house i and house (i-2) 
            # 2. Rob house i-1 and leave i
            # At any house, choose max of 2 options
            dp[i] = max((nums[i-1] + dp[i-2]), dp[i-1])
        return dp[-1]