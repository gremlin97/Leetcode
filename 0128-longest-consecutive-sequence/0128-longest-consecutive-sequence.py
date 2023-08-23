class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Implementing using a HashSet
        
        if nums == []:
            return 0
        
        s = set(nums)
        maxseq = 0
        
        for x in nums:
            if x-1 in s:
                continue
                
            currseq = 1
            
            while x+1 in s:
                currseq += 1
                x += 1
            
            if currseq > maxseq:
                maxseq = currseq
            
        
        return maxseq
            
            
                
            