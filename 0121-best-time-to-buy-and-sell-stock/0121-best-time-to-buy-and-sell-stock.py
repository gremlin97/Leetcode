class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            diff = prices[i] - curr
            max_profit = max(diff, max_profit)
            curr = min(curr, prices[i])
            
        return max_profit
            
        