class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        fptr = 0
        lptr = n - 1
        result = 0
        while fptr < lptr:
            vol = min(heights[fptr], heights[lptr]) * (lptr - fptr)
            if vol > result:
                result = vol
            if heights[fptr] < heights[lptr]:
                fptr += 1
            else:
                lptr -= 1
        return result