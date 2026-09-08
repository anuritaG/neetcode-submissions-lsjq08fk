class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for idx in range(len(nums)):
            num = nums[idx]
            if num in pos and idx - pos[num] <= k:
                return True
            pos[num] = idx
        return False