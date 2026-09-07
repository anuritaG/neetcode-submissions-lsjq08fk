class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buyPtr, sellPtr = 0, 0
        buy = prices[0]
        res = 0
        for price in prices:
            if price >= buy:
                res += (price - buy)
            buy = price

        return res


