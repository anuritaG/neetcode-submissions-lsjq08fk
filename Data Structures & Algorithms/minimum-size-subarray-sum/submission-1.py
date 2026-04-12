class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lptr, rptr = 0, 0
        sumSubArray = 0
        minLen = len(nums)
        for rptr in range(len(nums)):
            sumSubArray += nums[rptr]
            while lptr<=rptr and sumSubArray >= target:
                minLen = min(minLen, rptr - lptr + 1)
                sumSubArray -= nums[lptr]
                lptr += 1

        if lptr == 0 and rptr == len(nums)-1 and  sumSubArray < target:
            minLen = 0
        return minLen


        