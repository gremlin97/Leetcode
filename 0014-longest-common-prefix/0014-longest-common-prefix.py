class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        flag = True
        
        min_len = float('inf')
        for x in strs:
            min_len = min(len(x), min_len)
        
        for j in range(min_len):
            match_case = strs[0][j] 
            for i in range(len(strs)):
                if strs[i][j] == match_case and i == (len(strs)-1):
                    res += match_case
                elif strs[i][j] != match_case: 
                    flag = False
                    break
            if not flag: break
        return res
                
        