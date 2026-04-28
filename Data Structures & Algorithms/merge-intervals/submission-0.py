class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        for interval in intervals:
            lastEnd = res[-1][1]
            # If the current interval seen, has a start time <= ending of the last interval
            if interval[0] <= lastEnd:
                res[-1][1] = max(interval[1], lastEnd)
            else:
                # Non-overlapping
                res.append(interval)
        return res