class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The max area is basically the min(height[l], height[r]) * (r-l)
        # We start with max. gap between l and r and 
        # as we decrease the (r-l), we try to increase the min(height[l], height[r])
        lptr, rptr = 0, len(heights) - 1
        res = 0
        while rptr > lptr:
            res = max(res, (rptr - lptr) * min(heights[lptr], heights[rptr]))
            if heights[lptr] < heights[rptr]:
                lptr += 1
            else:
                rptr -= 1
        return res
        