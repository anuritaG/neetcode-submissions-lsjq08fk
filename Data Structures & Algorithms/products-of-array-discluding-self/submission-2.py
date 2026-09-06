class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        preMul = [1 for _ in range(n)]
        postMul = [1 for _ in range(n)]
        preMul[0] = nums[0]
        postMul[n-1] = nums[n-1]
        for idx in range(1, n):
            preMul[idx] = preMul[idx-1] * nums[idx]
        for idx in range(n-2, 0, -1):
            postMul[idx] = postMul[idx+1] * nums[idx]

        res = []
        for idx in range(n):
            mul = 1
            if idx > 0 :
                mul = mul * preMul[idx-1]
            if idx < n-1:
                mul = mul * postMul[idx+1]
            res.append(mul)
        return res
