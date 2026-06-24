class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        def recur(start):
            if len(subset) == k:
                res.append(subset.copy())
                return
            for i in range(start, n+1):
                subset.append(i)
                recur(i+1)
                
                subset.pop()
        recur(1)
        return res
