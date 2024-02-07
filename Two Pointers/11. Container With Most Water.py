# My solution with a hint
# The deal with this question is you have to understand:

# You have to move the smaller hight so that you can calculate max
# starting from far left to far right 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l<r:
            left = height[l]
            right = height[r]
            res = max(res, min(left, right) *  (r - l))
            if left >=right:
                r -= 1
            else:
                l += 1
        return res

        