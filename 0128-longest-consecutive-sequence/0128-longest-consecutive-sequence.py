class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        maxseq = 1 
        res = 1
        nums = sorted(nums)
        print(nums)
        for i in range(1, len(nums)):
            print('Res:',res)
            print(nums[i],nums[i-1])
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                res += 1
            else:
                if res > maxseq:
                    print('Yes')
                    maxseq = res
                    res = 1
                else:
                    res = 1
        
        if res > maxseq:
            maxseq = res
        
        
        return maxseq
                