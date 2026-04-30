class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = 0
        n = len(intervals)
        # Sort the intervals based on end time.
        # Choose the interval with the first finish time
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                res += 1
        return res