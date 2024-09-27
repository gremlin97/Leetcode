class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # c(n) = min(c(n-1),c(n-2)) + cost(n)
        
        # def recur(n):
        #     if n<=1:
        #         return cost[0]
        #     return min(recur(n-1), recur(n-2)) + cost[n-1]
        # return recur(len(cost))
        n = len(cost)
        @lru_cache()
        def solve(idx):
            if idx >= n:
                return 0
            if idx ==n-1:
                return cost[n-1]
            return min(solve(idx + 1), solve(idx + 2)) + cost[idx]
        return min(solve(0), solve(1))