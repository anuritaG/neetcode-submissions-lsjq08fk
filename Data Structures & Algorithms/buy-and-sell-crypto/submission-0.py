class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix = [0]*len(prices)
        prefix[0] = prices[0]
        for i in range(1, len(prices)):
            prefix[i] = min(prices[i], prefix[i-1])
        result = 0
        for i in range(len(prices)):
            profit = prices[i] - prefix[i]
            result = max(result, profit)
        return result


        