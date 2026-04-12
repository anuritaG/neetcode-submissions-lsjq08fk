class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = set()
        lptr, rptr = 0, 0
        maxLen = 0
        for rptr in range(len(s)):
            if s[rptr] in charMap:
                maxLen = max(len(charMap), maxLen)
                while lptr < rptr and s[lptr] != s[rptr]:
                    charMap.remove(s[lptr])
                    lptr += 1
                charMap.remove(s[lptr])
                lptr += 1
            charMap.add(s[rptr])
            rptr += 1
        maxLen = max(len(charMap), maxLen)
        return maxLen


        