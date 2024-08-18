class Solution:
    def hammingWeight(self, n: int) -> int:
        b = str(bin(n))[2:]
        print(b)
        res = 0
        
        for x in b:
            if x == '1':
                res += 1
        return res