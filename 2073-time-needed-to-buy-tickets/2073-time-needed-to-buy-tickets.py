class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        val = tickets[k]
        res = 0
        for i, x in enumerate(tickets):
            if i <= k:
                res += min(val, x)
            else:
                res += min(val-1, x)
        return res

        