class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        pick = [False] * len(nums)
        def dfs(perm):
            if len(perm) == len(nums):
                print("perm", perm)
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(perm)
                    perm.pop()
                    dfs(perm)
                    pick[i] = False
        dfs([])
        return res
