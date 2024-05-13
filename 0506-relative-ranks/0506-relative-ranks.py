class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []
        s = sorted(score, reverse = True)
        r = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + list(range(4,len(s)+1))
        z = dict(zip(s,r))
        for x in score:
            if type(z[x]) != string:
                res.append(str(z[x]))
            else:
                res.append(str(z[x]))
        return res
        
        