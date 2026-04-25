class Solution:
    def numSquares(self, n: int) -> int:
        # 1D DP solution: Iterate through i:1...n and find number of least sq
        # required to build i

        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for s in range(1, i+1):
                sq = s*s
                if sq > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i-sq])
        return dp[n]

        