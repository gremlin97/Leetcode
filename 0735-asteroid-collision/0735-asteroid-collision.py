class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            while stack and stack[-1]>0 and x<0:
                if stack[-1] + x < 0:
                    stack.pop()
                elif stack[-1] + x > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(x)
        
        return stack