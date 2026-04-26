class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curLen, maxLen = 0, 0
        sign = 0
        # if arr[i] < arr[i+1] --> sign = -1
        # if arr[i] > arr[i+1] --> sign = 1
        # if the prev sign is not opposite of the current sign
        # discard it and start with one len.
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                if sign == 1:
                    curLen += 1
                else:
                    curLen = 1
                sign = -1
            elif arr[i] > arr[i+1]:
                if sign == -1 :
                    curLen += 1
                else:
                    curLen = 1
                sign = 1
            else:
                curLen = 0
                sign = 0
            print(arr[i], " ", curLen, " ", sign)
            maxLen = max(maxLen, curLen)
        return maxLen + 1



            
