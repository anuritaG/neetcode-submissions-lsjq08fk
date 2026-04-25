class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # If we take the abs value of each number, if we iterate through each
        # number and multiply it, the value is always non-decreasing.
        # For the sign, we also need to store the min. value because multiplying it
        # with another - sign can make it max. as well
        curMax, curMin = 1, 1
        maxVal = nums[0]
        for num in nums:
            tmp = curMax
            curMax = max(curMax*num, num, curMin*num)
            curMin = min(tmp*num, num, curMin*num)
            maxVal = max(maxVal, curMax)
        return maxVal
        