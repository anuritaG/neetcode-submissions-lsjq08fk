class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixMax, postFixMax = [0] * n, [0] * n
        prefixMax[0] = height[0]
        postFixMax[n-1] = height[n-1]
        for i in range(1, len(height)):
            prefixMax[i] = max(prefixMax[i-1], height[i])
        for i in range(len(height) - 2, -1, -1):
            postFixMax[i] = max(postFixMax[i+1], height[i])
        result = 0
        print(prefixMax)
        for i in range(n):
            result += min(prefixMax[i], postFixMax[i]) - height[i]
        return result     


        