class Solution:
    def numSquares(self, n: int) -> int:
        # Check if the number is any form of 4k(8m+7)
        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        def isSquareNum(num):
            s = int(math.sqrt(num))
            return s * s == num

        if isSquareNum(n):
            return 1

        i = 1
        # If number is sq(a) + sq(b)
        while i * i <= n:
            if isSquareNum(n - i * i):
                return 2
            i += 1

        return 3