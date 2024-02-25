class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        memo = [-1] * (amount + 1)
        coins = sorted(coins, reverse=True)
        
        @lru_cache
        def dfs(t):
            
            if memo[t]>=0:
                return memo[t]
            
            if t == 0:
                return 0
            
            shortestCombination = float('inf')
            
            for i in range(len(coins)):
                if coins[i] <= t:
                    remainder = t - coins[i]
                    if memo[remainder]>=0:
                        remainderCombination = memo[remainder] + 1
                    else:
                        remainderCombination = dfs(remainder) + 1
                        
                    if remainderCombination < shortestCombination:
                        shortestCombination = remainderCombination
            
            memo[t] = shortestCombination
            return shortestCombination
        
        
        res = dfs(amount)
        
        if res == float('inf'):
            return -1
        return res
                    
        
            
            