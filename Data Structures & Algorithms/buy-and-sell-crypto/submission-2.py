class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy when the price is lowest and sale at highest.
        buy, sell = prices[0], prices[0]
        maxProfit = 0
        for price in prices[1:]:
            # If the price is less than buyPrice, sell the previously 
            # bought coin and buy the new one.
            if price < buy:
                profit = sell - buy
                buy = price
                sell = price
                maxProfit = max(maxProfit, profit)
            # If the price is more than the sell, change the sell price
            if price > sell:
                sell = price
            
        maxProfit = max(maxProfit, sell-buy)
        return maxProfit



        