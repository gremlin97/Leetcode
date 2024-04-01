class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] + asteroid == 0:
                        stack.pop()
                        break
                    elif stack[-1] + asteroid < 0:
                        stack.pop()
                    else:
                        break
                else:
                    stack.append(asteroid)
                    
        return stack
#         stack = []
        
#         for x in asteroids:
#             print(stack)
#             if len(stack) == 0:
#                 stack.append(x)
#             elif stack[-1] < 0:
#                 stack.append(x)
#             elif (stack[-1] + x  == 0):
#                 stack.pop()
#             elif (stack[-1] - x > stack[-1]):
#                 if abs(stack[-1]) < abs(x):
#                     stack.pop()
#                     stack.append(x)
#             else:
#                 stack.append(x)
                    
#         return stack
            
                    