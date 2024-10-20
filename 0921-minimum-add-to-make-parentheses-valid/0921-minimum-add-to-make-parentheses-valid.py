class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
    
        for x in s:
            print(st)
            if not st:
                st.append(x)
            elif x == ')' and st[-1] == '(' and st:
                st.pop()
            else:
                st.append(x)
        return len(st)
                
        