class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        hashmap = {}
        
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
            
        _hashmap = {k:v for k,v in sorted(hashmap.items(), key = lambda x : x[1], reverse = True)}
        
        _hashmap = [k for k,v in _hashmap.items()]
        
        for i in range(0, k):
            res.append(_hashmap[i])
        
        return res

        
            
            
        