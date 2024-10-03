class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        
        m = float('inf')
        for x in strs:
            m = min(len(x),m)
            
        print(m)
            
        for i in range(m):
            curr = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != curr:
                    return res
            res += curr
        return res
        