class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # d = Counter(arr)
        d = {}
        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        print(d)
        return (len(d.values()) == len(set(d.values())))