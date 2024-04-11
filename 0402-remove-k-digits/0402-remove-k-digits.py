class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        sys.set_int_max_str_digits(50000)
        
        stack = []
        
        for x in num:
            while stack and k>0 and stack[-1] > x:
                k -= 1
                stack.pop()
            stack.append(x)
        
        res = ''.join(stack)
        res = res[:len(stack)-k]
        if res:
            return str(int(res))
        return '0'
                