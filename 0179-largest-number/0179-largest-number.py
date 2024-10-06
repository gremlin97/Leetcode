class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def fx(x,y):
            if x+y>y+x: return 1
            elif x == y: return 0
            else: return -1
        
        n = [str(x) for x in nums]
        n.sort(key = cmp_to_key(fx), reverse=True)
        res = ''.join(n).lstrip('0')
        if not res:
            return '0'
        return res