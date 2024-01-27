class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        res, flag = '', False
        strs = sorted(strs)
        
        for i in range(0, len(strs[0])):
            base = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != base:
                    flag = True
                    return res
            res += strs[0][i]
            
        if flag:
            return ''
        else:
            return res
                