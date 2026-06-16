class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 2 branches:BR 1 take the current value,BR 2: do not take the current value
        # But i can be chosen at most once, so always increase i's value
        # Main issue with this: duplication of sets: basically if we have [1,1,2]
        # when we are skipping the first 1, we should skip the second 1 as well, as 1,2 
        # has already been considered, we just consider sets where both 1's [dfs(i+1, amt-nums[i])]
        # or none of them dfs[i+1, nums[i]] are included. For the single 1's running [dfs(i+1, amt-nums[i])]
        # once for every duplicate element should be sufficient
        candidates.sort()
        subset = []
        res = []
        def dfs(i, amt):
            if amt == 0:
                res.append(subset.copy())
                return
            if amt <= 0 or i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1, amt-candidates[i])
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            subset.pop()
            dfs(j, amt)
        dfs(0, target)
        return res