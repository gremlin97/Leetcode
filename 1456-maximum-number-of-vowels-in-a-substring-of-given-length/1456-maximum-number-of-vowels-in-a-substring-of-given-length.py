class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u'] 
        l = 0
        r = l + k - 1
        max_vow = curr_vow = len([x for x in s[l:r+1] if x in vowels])
        print(curr_vow)
        
        while(r < len(s)-1):
            l+=1
            r+=1
            if s[r] in vowels:
                curr_vow += 1
            if s[l-1] in vowels:
                curr_vow -= 1
            max_vow = max(curr_vow, max_vow)
        
        return max_vow
                
            
        