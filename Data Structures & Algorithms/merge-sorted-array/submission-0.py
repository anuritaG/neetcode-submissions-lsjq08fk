class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        fPtr, sPtr = m - 1, len(nums2) - 1
        tPtr = len(nums1) - 1
        while fPtr >= 0 and sPtr >= 0:
            if nums1[fPtr] > nums2[sPtr]:
                nums1[tPtr] = nums1[fPtr]
                fPtr -= 1
            else:
                nums1[tPtr] = nums2[sPtr]
                sPtr -= 1
            tPtr -= 1
        while sPtr >= 0:
            nums1[tPtr] = nums2[sPtr]
            sPtr -= 1
            tPtr -= 1

        
        