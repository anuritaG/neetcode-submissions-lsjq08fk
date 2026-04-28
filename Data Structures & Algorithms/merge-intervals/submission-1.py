class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sweep Line Algorithm
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1   
        
        res = []
        # stores a particular interval value
        interval = []
        have = 0
        for i in sorted(mp):
            if not interval:
                interval.append(i)
            have += mp[i]
            # all overlapping intervals that had started at i, has ended
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        return res
