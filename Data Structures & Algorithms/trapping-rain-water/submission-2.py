class Solution:
    def trap(self, height: List[int]) -> int:
        # The water trapped in a particular bar is 
        # min(maxHeight[left of that bar], maxHeight[right of that bar]) - height of bar
        # Compute and store the maxHeight left and right of each bar
        n = len(height)
        maxHeightLeft, maxHeightRight = [0]*n, [0]*n
        for idx in range(1, n):
            maxHeightLeft[idx] = max(height[idx-1], maxHeightLeft[idx-1])
        for idx in range(n-2,0,-1):
            maxHeightRight[idx] = max(height[idx+1], maxHeightRight[idx+1])
        resVolume = 0
        for idx in range(n):
            volume = min(maxHeightLeft[idx], maxHeightRight[idx]) - height[idx]
            if volume > 0:
                resVolume += volume
        return resVolume


        