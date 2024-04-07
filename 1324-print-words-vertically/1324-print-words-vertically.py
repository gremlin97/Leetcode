class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        max_substring_len = 0
        for x in s:
            max_substring_len = max(max_substring_len, len(x))
        res = []        
        # print(max_substring_len)
            
        for i in range(max_substring_len):
            temp = []
            for j in range(len(s)):
                # print(s[j],i, temp)
                if i > (len(s[j]) - 1):
                    temp.append(' ')
                else:
                    temp.append(s[j][i])
            
            res.append(''.join(temp).rstrip())
        
        return res
        