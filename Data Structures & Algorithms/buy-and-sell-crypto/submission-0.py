class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        
        for i in prices:
            
            profit = i - min_price
            
            if i < min_price:
                min_price = i
            
            if profit > max_profit:
                max_profit = profit
            #print(i, min_price, profit, max_profit)
                
        return max_profit if max_profit > 0 else 0