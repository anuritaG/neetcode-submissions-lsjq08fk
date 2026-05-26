class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        fptr, lptr = 0, 0
        maxf = 0
        result = 0
        count = {}
        while lptr < n:
            if s[lptr] not in count:
                count[s[lptr]] = 0
            count[s[lptr]] += 1
            maxf = max(maxf, count[s[lptr]])
            while (lptr + 1 - fptr) - maxf > k:
                count[s[fptr]] -= 1
                fptr += 1
            result = max(result, lptr - fptr + 1)
            lptr +=1 
        return result
        