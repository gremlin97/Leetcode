class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
                
        common_set = list(set(order).intersection(set(s)))
        common_list = [x for x in order if x in common_set]
        other = list(set([x for x in list(s) if x not in common_set]))
        other.sort()
        union = common_list + other
        print(d)
        print(union, common_list, other)
        
        res = ''
        for x in union:
            res = res + x * d[x]
        
        return res