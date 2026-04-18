class StockSpanner:

    def __init__(self):
        self.stack = [] # pair of price and span
        

    def next(self, price: int) -> int:
        span = 0
        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            least_price = self.stack.pop()
            span += least_price[1]
        
        self.stack.append((price, span+1))
        return span + 1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)