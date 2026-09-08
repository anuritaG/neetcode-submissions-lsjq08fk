class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        pos = {}
        fptr, lptr = 0, 0
        while lptr < len(s):
            # print("fptr", fptr,  " ", lptr," ",s[lptr], " res", res)
            if s[lptr] not in pos or pos[s[lptr]] < fptr:
                pos[s[lptr]] = lptr
            else:
                res = max(res, lptr-fptr)
                fptr = pos[s[lptr]] + 1
                pos[s[lptr]] = lptr
            lptr += 1
        res = max(res, lptr-fptr)
        return res