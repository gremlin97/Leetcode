class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            print(x)
            string = ''.join(sorted(list(x)))
            if string in hashmap:
                hashmap[string].append(x)
            else:
                hashmap[string] = [x]

        return hashmap.values()
                    
                    
            
            
        