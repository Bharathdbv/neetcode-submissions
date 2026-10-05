class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        min_price = prices[0]
        
        for price in prices[1:]:
            profit = max(profit, price - min_price)
            
            min_price = min(min_price, price)
        
        return profit
