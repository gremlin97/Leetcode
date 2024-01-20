class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for x in arr:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x]+=1
            
        if len(hashmap.values()) == len(set(list(hashmap.values()))):
            return True
        else:
            return False