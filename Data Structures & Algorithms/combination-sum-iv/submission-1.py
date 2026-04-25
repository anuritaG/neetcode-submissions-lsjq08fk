class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 1D DP: starting with j: 0 -> target, we check no. of way to make k
        # For a j, for each num, no. of ways = + dp(j-num) 
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i>=num:
                    dp[i] += dp[i-num]
        return dp[-1]