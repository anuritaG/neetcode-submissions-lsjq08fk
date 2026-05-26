class Solution:
    def check(self, count):
        for key in count:
            if count[key] != 0:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for char1 in s1:
            count[char1] = 1 + count.get(char1, 0)
        lptr, rptr = 0, 0
        for rptr in range(len(s2)):
            # s2[rptr] part of count, count > 0 - decrease it
            # s2[rptr] part of count, but count < 0 - slide 1 at a time and increase count and check.
            # s2[rptr] not part of s1. - substring seen till now invalid
            char = s2[rptr]
            print(lptr, rptr, s2[lptr], s2[rptr], count)
            if char in count and count[char] > 0:
                count[char] -= 1
                if self.check(count) == True:
                    return True
            else:
                while lptr < rptr:
                    if s2[lptr] == char:
                        break
                    if s2[lptr] in count:
                        count[s2[lptr]] += 1
                    lptr += 1 
        return self.check(count)