class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        resArr = [0] * len(arr)
        for i in range(len(arr)):
            resArr[i] = abs(arr[i]-x)
        lptr = 0
        rptr = len(resArr) - 1
        while (rptr-lptr+1) > k:
            if resArr[lptr] > resArr[rptr]:
                lptr += 1
            else:
                rptr -= 1
        return arr[lptr:rptr+1]



        

        