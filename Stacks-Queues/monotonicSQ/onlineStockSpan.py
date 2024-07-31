# ### ONLINE STOCK SPAN 

# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:
 

# https://leetcode.com/problems/online-stock-span/description/

class StockSpanner:

    def __init__(self):
        self.stack = [] # [(price, day)]
        self.day = 0
        

    def next(self, price: int) -> int:
        #self.stocks.append(price)
        #print(self.stack, price)
        self.day += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
    
        if not self.stack:
            span = self.day
        else:
            span = self.day - self.stack[-1][1]
        
        self.stack.append((price, self.day))
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
