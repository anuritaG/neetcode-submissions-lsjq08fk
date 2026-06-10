class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        idx = 0
        while n > 26:
            idx += 1
            n = int(n/26)
        res = ""
        # res = 0
        print("idx", idx)
        while idx >= 0:
            power = math.pow(26, idx)
            # print("26 ",power)
            num = int(columnNumber / (power))
            res += chr(num + 64)
            # print("res", res)
            # print(chr(res+64))
            # print("res", res)
            columnNumber = columnNumber % power
            
            idx -= 1
        # print(res)

        return res