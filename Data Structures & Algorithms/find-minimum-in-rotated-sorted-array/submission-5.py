class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
        while low <= high:
            mid = (low + high) // 2
            # Reached either the first element or the last element.
            # Nowhere to move means: this is the min. one
            if mid == low and mid == high:
                return nums[mid]
            if nums[mid] < nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        