class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        i = 0
        while i < len(nums):
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            anchor = nums[i]
            diff = -nums[i]
            l, r = i+1, len(nums)-1
            
            while l<r:
                if nums[l] + nums[r] > diff:
                    r-=1
                elif nums[l] + nums[r] < diff:
                    l+=1
                else:
                    res.append([anchor, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                        
                    
            i+=1
        return res                            
                    
                    
        