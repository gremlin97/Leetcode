class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currnum = 0; currstring = ''
        for x in s:
            if x.isdigit():
                currnum = currnum*10 + int(x)
            elif x == '[':
                stack.append(currnum)
                stack.append(currstring)
                currnum = 0
                currstring = ''
            elif x == ']':
                prevstring = stack.pop()
                dig = stack.pop()
                currstring = prevstring + currstring*dig
            else:
                currstring += x

        return currstring
                
        