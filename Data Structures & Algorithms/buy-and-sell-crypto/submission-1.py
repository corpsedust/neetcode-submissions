class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0            #cash 
        min_price = float('inf') #hold
        
        for p in prices:
            
            #profit = p - min_price  
            
            # if p < min_price:
            #     min_price = p
                
            min_price = min(min_price, p)
            
            # if profit > max_profit:
            #     max_profit = profit
            
            max_profit = max(max_profit, p - min_price)
            
            #print(p, min_price, profit, max_profit)
                
        return max_profit