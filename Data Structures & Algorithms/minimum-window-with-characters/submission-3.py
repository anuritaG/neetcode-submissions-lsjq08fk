class Solution:
    def containsAllChar(self, charMap):
        for char, freq in charMap.items():
            if charMap[char] > 0:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        charMap = {}
        for char in t:
            charMap[char] = 1 + charMap.get(char, 0)
        fptr, lptr = -1,0
        minLen = len(s)
        resfPtr = -1 
        result = ""
        reslPtr = -1
        # update lptr till all chars are atleast 0, some can be < 0
        # update fptr, if one of char > 0, break the result.
        # start from fptr = fptr+1, and again
        for lptr in range(len(s)):
            if s[lptr] in charMap:
                charMap[s[lptr]] -= 1
            containsSubStr = self.containsAllChar(charMap)
            if containsSubStr:
                while fptr<lptr:
                    fptr += 1
                    if s[fptr] in charMap:
                        charMap[s[fptr]] += 1
                        if charMap[s[fptr]] > 0:
                            # length = min(result, lptr-fptr+1)
                            if lptr-fptr+1 <= minLen:
                                minLen = lptr - fptr + 1
                                resfPtr = fptr
                                reslPtr = lptr
                            break
        if resfPtr != -1 and reslPtr != -1:
            result += s[resfPtr: reslPtr+1]
        return result
        



