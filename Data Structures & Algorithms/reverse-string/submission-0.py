class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        startPtr = 0
        endPtr = len(s) - 1
        while startPtr < endPtr :
            temp = s[startPtr]
            s[startPtr] = s[endPtr]
            s[endPtr] = temp
            startPtr += 1
            endPtr -= 1
            