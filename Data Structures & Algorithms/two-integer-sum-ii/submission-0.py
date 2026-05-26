class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            add = numbers[l] + numbers[r]
            if add == target:
                return [l+1, r+1]
            if add < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]