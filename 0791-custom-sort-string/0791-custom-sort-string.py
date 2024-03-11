from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = Counter(s)
        common_set = list(set(order).intersection(set(s)))
        common_list = [x for x in order if x in common_set]
        other = list(set([x for x in list(s) if x not in common_set]))
        union = common_list + other
        
        res = ''
        for x in union:
            res = res + x * d[x]
        
        return res