class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # increasinhg - do not sell. 
        # decreasing - do not buy
        # increasing -> decreasing --> sell it
        buy = 0
        sell = 0
        result = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx-1]:
                sell = idx
            if prices[idx] < prices[idx-1]:
                # selling the stocks
                result = result + prices[sell] - prices[buy]
                buy = idx
                sell = idx
        result = result + prices[sell] - prices[buy]
        return result