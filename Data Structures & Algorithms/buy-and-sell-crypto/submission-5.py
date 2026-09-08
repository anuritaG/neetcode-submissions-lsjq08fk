class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], prices[0]
        res = 0
        for price in prices:
            print(price, "buy,", buy, "   ", sell)
            if price < buy:
                res = max(res, sell-buy)
                buy = price
                sell = price
            if price > sell:
                sell = price
        res = max(res, sell-buy)
        return res
        