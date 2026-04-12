class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        lptr, rptr = 0, 0
        maxLen = 0
        # Check if the letter already exists in charMap
        for rptr in range(len(s)):
            # If letter present change the left ptr of substring to point to
            # next letter of the duplicate letter and store the new index of the 
            # duplicate letter
            if s[rptr] in charMap and charMap[s[rptr]] >= lptr:
                maxLen = max(maxLen, rptr - lptr)
                lptr = charMap[s[rptr]] + 1
            charMap[s[rptr]] = rptr
            rptr += 1
        maxLen = max(rptr - lptr, maxLen)
        return maxLen


        