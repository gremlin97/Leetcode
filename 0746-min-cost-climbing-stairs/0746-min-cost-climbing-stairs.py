class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def minCost(n):
            if n<2:
                return cost[n]
            return min(minCost(n-1), minCost(n-2)) + cost[n]
        return min(minCost(len(cost)-1), minCost(len(cost)-2)) 