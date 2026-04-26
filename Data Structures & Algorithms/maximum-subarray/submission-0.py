class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # When the sum reaches a negative, ditch the old subarray
        curSum , maxSum = 0, nums[0]
        for num in nums:
            curSum += num
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
        return maxSum