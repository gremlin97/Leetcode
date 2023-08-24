class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        
        for i in range(0, len(nums)):
            l = i+1
            r = len(nums)-1
                    
            while(l<r):
                temp = []
                if nums[l] + nums[r] == -nums[i]:
                    temp.extend([nums[l],nums[r],nums[i]])
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                    
                    l+=1
                    r-=1
                    
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
            
        return res
                    
        