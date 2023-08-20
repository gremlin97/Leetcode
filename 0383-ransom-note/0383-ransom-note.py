class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        
        for x in magazine:
            if x in hashmap1:
                hashmap1[x] += 1
            else:
                hashmap1[x] = 1
        
        for x in ransomNote:
            if x in hashmap2:
                hashmap2[x] += 1
            else:
                hashmap2[x] = 1
        
        print(hashmap1, hashmap2)

        for x in ransomNote:
            if x not in hashmap1:
                return False
            if x in hashmap1:
                if hashmap1[x] < hashmap2[x]:
                    return False
                
        
        return True
        
        
        
        
        
        