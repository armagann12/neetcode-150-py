# My solution with a little help

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # You dont have to check the other way around
            while stack and a < 0 and stack[-1] > 0:
                # You can also check diff here
                if abs(a) > stack[-1]: 
                    stack.pop()
                elif abs(a) == stack[-1]:
                    stack.pop()
                    a = 0
                else:
                    a = 0
            if a != 0:
                stack.append(a)

        return stack