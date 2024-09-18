class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        print(nums)
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i>0:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    l += 1
                    
        return res

                    
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        