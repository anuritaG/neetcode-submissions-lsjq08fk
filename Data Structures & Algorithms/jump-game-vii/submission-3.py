class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        # Sliding window + greedy
        # We store True/False in a DP
        # In each position, we mark from i+minJump, i+maxJmp to True/False
        # Care to be taken such that i+minJump, i+maxJmp is not overlapped.
        dp = [False] * len(s)
        dp[0] = True
        j = 0
        for i in range(len(s)):
            # can not reach this place -> can not go any place from this
            if dp[i] == False:
                continue
            j = max(j, i+minJump)
            while j <= i + maxJump and j < len(s):
                if s[j] == '0':
                    dp[j] = True
                j += 1
               
        return dp[-1]