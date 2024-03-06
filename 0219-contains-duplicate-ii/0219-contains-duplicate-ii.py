class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = []
                d[nums[i]].append(i)
            else:
                d[nums[i]].append(i)
        
        print(d)
                
        
        for key, value in d.items():
            if len(value) >= 2: 
                for i in range(len(value) - 1):
                    if abs(value[i] - value[i+1]) <= k:
                        return True
            
        return False
            
        