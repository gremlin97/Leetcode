class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res.append(matrix[i][j])
        
        l, r = 0 , len(res)-1
        
        while l<=r:
            mid = l + (r-l)//2
            if target == res[mid]:
                return True
            elif res[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        