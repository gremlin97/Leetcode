class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        # print(sorted(list(d.values())), sorted(list(set(d.values()))))
        return (sorted(list(d.values())) == sorted(list(set(d.values()))))