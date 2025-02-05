class Solution(object):
    def maxProfit(self, prices):
        # Edge cases
        if len(prices) < 2:
            return 0

        # Keep track of max profit encountered
        max_profit = 0

        # Start by buying on day 1
        buy = prices[0]

        for price in prices:
            # Keep track of lowest possible buy price
            if price < buy:
                buy = price
            
            # Compare current profit to max profit
            current_profit = price - buy
            max_profit = max(max_profit, current_profit)
        
        return max_profit
