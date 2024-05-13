class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # res = []
        # s = sorted(score, reverse = True)
        # r = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + list(range(4,len(s)+1))
        # z = dict(zip(s,r))
        # for x in score:
        #     if type(z[x]) != string:
        #         res.append(str(z[x]))
        #     else:
        #         res.append(str(z[x]))
        # return res
        
        
        
        res = []
        heap = []
        for i,v in enumerate(score):
            heapq.heappush(heap,(-v, i))
        res = [0] * len(score) 
        r = 1
        while heap:
            if r == 1:
                res[heapq.heappop(heap)[1]] = 'Gold Medal'
            elif r == 2:
                res[heapq.heappop(heap)[1]] = 'Silver Medal'
            elif r == 3:
                res[heapq.heappop(heap)[1]] = 'Bronze Medal'
            else:
                res[heapq.heappop(heap)[1]] = str(r)
            r += 1
        
        return res
                
        
        
        