class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {'(':')','[':']','{':'}'}
        if ')' in d:
            print('Yes')
        
        for x in s:
            if x in d:
                st.append(x)
            elif (x not in d) and st:
                print('Inside')
                if d[st[-1]] == x:
                    st.pop()
                else:
                    return False
            else:
                return False
        print('Here')
        if st:
            return False
        return True
            
        