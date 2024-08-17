class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = ''.join([str(x) for x in digits])
        d = list(str(int(d) + 1))
        d = [int(x) for x in d]
        return d
                
        