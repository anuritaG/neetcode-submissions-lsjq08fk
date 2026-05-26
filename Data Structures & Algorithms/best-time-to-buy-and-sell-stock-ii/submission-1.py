class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIdx = 0
        sellIdx = 0
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx-1]:
                sellIdx = idx
            if prices[idx] < prices[idx-1]:
                # selling the stocks
                profit = profit + prices[sellIdx] - prices[buyIdx]
                buyIdx = idx
                sellIdx = idx
        profit = profit + prices[sellIdx] - prices[buyIdx]
        return profit