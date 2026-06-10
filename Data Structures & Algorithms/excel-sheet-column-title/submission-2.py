class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        idx = 0
        while n > 26:
            idx += 1
            n = int(n/26)
        res = ""
        while idx >= 0:
            power = math.pow(26, idx)
            num = int(columnNumber / (power))
            # conversion to alphabets
            res += chr(num + 64)
            columnNumber = columnNumber % power
            idx -= 1
        return res