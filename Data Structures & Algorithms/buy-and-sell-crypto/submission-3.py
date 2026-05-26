class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy when the price is lowest and sale at highest.
        lPtr, rPtr = 0, 0
        maxProfit = 0
        while rPtr < len(prices):
            # If the price is more than the current buy price, compute the profit
            # If not, buy the new item
            if prices[rPtr] < prices[lPtr]:
                lPtr = rPtr
            else:
                maxProfit = max(maxProfit, prices[rPtr] - prices[lPtr])
            rPtr += 1

        # for price in prices[1:]:
        #     
        #     if price < buy:
        #         buy = price
        #         sell = price
        #     else:
        #         sell += 1
        #         maxProfit = max(maxProfit, sell-buy)
            
        # maxProfit = max(maxProfit, sell-buy)
        return maxProfit



        