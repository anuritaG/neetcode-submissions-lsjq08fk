class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # DP solution is to check which numbers can be joined to form the target
        # dp[i][j] can the first i no.s form a sum of j
        # at any (i,j) we have 2 options: skip num(i) dp(i,j) = dp(i-1,j)
        # or if (j-i) >= 0 then select i, dp(i,j) = dp(i-1, j -nums(i)) 
        # basically, if we take i it becomes true only if the first (i-1) no. can sum to (j-nums(i)) target
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp=[[False] * (target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                if nums[i-1] <= j:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[n][target]
 
        