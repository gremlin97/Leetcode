class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # val = tickets[k]
        # res = val
        # tickets.pop(k)
        # for x in tickets:
        #     print(tickets, x, abs(x-val))
        #     res += min(val, abs(x-val))
        # return res
        return sum(min(x, tickets[k] if i <= k else tickets[k] - 1) for i, x in enumerate(tickets))