class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:cost[0], 1:cost[1]}
        def minCost(n):
            if n in memo:
                return memo[n]
            memo[n] = min(minCost(n-1), minCost(n-2)) + cost[n]
            return memo[n]
        
        return min(minCost(len(cost)-1), minCost(len(cost)-2)) 