class Solution:
    def isPalindrome(self, s: str) -> bool:
        startPtr = 0
        trimmedStr = ""
        indx = 0
        while indx < len(s):
            if s[indx].isalnum():
                trimmedStr = trimmedStr + s[indx].lower()
            indx += 1
        endPtr = len(trimmedStr) - 1
        while startPtr < endPtr:
            if trimmedStr[startPtr] != trimmedStr[endPtr]:
                return False
            startPtr += 1
            endPtr -= 1
        return True