class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # dp = [[-1,-1]] * 26: creates reference to the same rpw. changing one row changes everything
        dp = [[-1, 1] for _ in range(26)]
        # Store the first and last occurence of each alphabet
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if dp[idx][0] == -1:
                dp[idx][0] = i
            # if dp[idx][1] == -1:
            dp[idx][1] = i
        # # sort based on 1st occurence
        dp.sort()
        res = []
        firstIdx = 0
        lastIdx = 0
        # print(dp)
        for fp,lp in dp:
            if fp == -1:
                continue
            # print(fp, " ", lp)
            if fp <= lastIdx:
                lastIdx = max(lastIdx, lp)
            else:
                res.append(lastIdx-firstIdx+1)
                # print("lt", lastIdx, " ", firstIdx)
                firstIdx = fp
                lastIdx = lp
        # print(firstIdx, lastIdx)
        # print(res)
        res.append(lastIdx-firstIdx+1)
        return res

        