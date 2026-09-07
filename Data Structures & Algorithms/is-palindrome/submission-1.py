class Solution:
    def isPalindrome(self, s: str) -> bool:
        fptr = 0
        
        trimS = ""
        for char in s:
            if char.isalnum():
                trimS += char.lower()
        # print(trimS)
        lptr = len(trimS) - 1
        while fptr <= lptr:
            if trimS[fptr] != trimS[lptr]:
                return False
            fptr += 1
            lptr -= 1
        return True
        