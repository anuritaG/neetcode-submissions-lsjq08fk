class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        fptr, lptr = 0,0
        result = 0
        while lptr < len(s):
            char = s[lptr]
            if char in charMap and charMap[char] >= fptr:
                result = max(result, lptr-fptr)
                fptr = charMap[char] + 1
            charMap[char] = lptr
            lptr += 1
        result = max(result, lptr-fptr)
        return result

        