class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        
        sortedHashmap = dict(sorted(hashmap.items(),key=lambda x:x[1]))
        threshold = len(nums)//2
        for k,v in sortedHashmap.items():
            if v>threshold:
                return k