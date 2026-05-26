class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMul = [0 for _ in range(len(nums))]
        suffixMul = [0 for _ in range(len(nums))]
        mul = 1
        for indx in range(len(nums)):
            mul *= nums[indx]
            prefixMul[indx] = mul
        mul = 1
        for indx in range(len(nums)-1, 0 , -1):
            mul *= nums[indx]
            suffixMul[indx] = mul
        result = [0 for _ in range(len(nums))]
        for indx in range(len(nums)):
            if indx == 0:
                preMul = 1
            else:
                preMul = prefixMul[indx-1]
            if indx == len(nums)-1:
                sufMul = 1
            else:
                sufMul = suffixMul[indx+1]
            result[indx] = preMul * sufMul
        return result