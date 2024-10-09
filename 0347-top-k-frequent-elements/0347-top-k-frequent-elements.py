class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        n = [[-v,k] for k,v in d.items()]
        heapq.heapify(n)
        res = []
        
        while k:
            count, key = heapq.heappop(n)
            res.append(key)
            k -= 1
        
        print(res)
        return res
        
        
        