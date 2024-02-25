# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int: 
#         memo = [-1] * (amount + 1)
        
#         def dfs(t):
            
#             if memo[t]>=0:
#                 return memo[t]
            
#             if t == 0:
#                 return 0
            
#             shortestCombination = float('inf')
            
#             for i in range(len(coins)):
#                 print(memo)
#                 if coins[i] <= t:
#                     remainder = t - coins[i]
#                     if memo[remainder]>=0:
#                         remainderCombination = memo[remainder]
#                     else:
#                         remainderCombination = dfs(remainder)
#                         memo[remainder] = remainderCombination
                        
#                     if remainderCombination>=0:
#                         remainderCombination += 1
                     
#                         if remainderCombination<shortestCombination:
#                             shortestCombination = remainderCombination
                    
#             if shortestCombination ==  float('inf'):
#                 return -1

#             return shortestCombination
        
#         return dfs(amount)
                    
        
            
            
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining_amount):
            if remaining_amount in memo:
                return memo[remaining_amount]

            if remaining_amount < 0:
                return -1
            if remaining_amount == 0:
                return 0

            shortest_combination = float('inf')

            for coin in coins:
                remainder = remaining_amount - coin
                result = dfs(remainder)

                if result >= 0 and result < shortest_combination:
                    shortest_combination = result + 1

            memo[remaining_amount] = shortest_combination if shortest_combination != float('inf') else -1
            return memo[remaining_amount]

        return dfs(amount)
