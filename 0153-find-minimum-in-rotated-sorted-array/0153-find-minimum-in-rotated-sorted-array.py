class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1
        
        while l<r:
            mid = l + (r-l)//2

            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        
        return nums[l]
        
        
        # 3 4 5 1 2
        '''
        0, 4, mid = 4//2 = 2 (3,5,2)
        5>2
        
        0,2,4 -> 3,3,4 -> 3,3 
        
        4 5 1 2 3  (4,1,3) 1<3
        
        
        '''
        