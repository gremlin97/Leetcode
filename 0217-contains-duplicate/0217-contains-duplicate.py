class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for x in nums:
            if x in hashmap.keys():
                hashmap[x]+=1
                return True
            else:
                hashmap[x] = 1
        return False
        
         
        