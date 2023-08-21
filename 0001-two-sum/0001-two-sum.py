class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hashmap = {}
        
        for x in nums:
            hashmap[x] = target - x
        
        for x in nums:
            if hashmap[x] in nums:
                if nums.index(x) == nums.index(hashmap[x]):
                    if nums.count(x)>1: 
                        res.extend(sorted([nums.index(hashmap[x], nums.index(x) + 1), nums.index(x)]))
                        return res
                    else:
                        continue
                else:
                    res.extend(sorted([nums.index(hashmap[x]), nums.index(x)]))
                    return res
                    
                
        
            
        
        
        