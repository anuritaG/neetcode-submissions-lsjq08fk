class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # As k can be greater than nums
        def reverse(l, r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums)-1)

        