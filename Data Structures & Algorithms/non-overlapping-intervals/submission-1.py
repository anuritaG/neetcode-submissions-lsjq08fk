class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        i = 0
        j = 0
        res = 0
        n = len(intervals)
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                res += 1
        return res