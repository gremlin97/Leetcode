class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx_area = 0
        l, r = 0, len(height) - 1
        while l<r:
            # print(l, r, height[l], height[r])
            curr_area = (r-l) * min(height[l], height[r])
            mx_area = max(curr_area, mx_area)
            if height[l]<height[r]:
                l +=1 
            else:
                r -= 1
        
        return mx_area
        # 8 7 2 1
        '''
        
        a = 1*3 = 3
        a = 2*2 = 4
        
        
        '''
        