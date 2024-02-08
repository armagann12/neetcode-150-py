# Hard question
# Its about finding ith elements left and right biggest elements min value and subtracting form the ith element


# Solution: Using extra arrays
# Calculating leftMax and rightMax values with two extra arrays
# Than taking min value of them and substracting from the element
# And that is the rain water being trapped
# Needs refactoring
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxL = [0]
        maxR = [0]
        for h in height:
            maxL.append(max(max(maxL), h))
        for h in height[::-1]:
            maxR.append(max(max(maxR), h))
        maxR = maxR[::-1]
        for i in range(len(height)):
            minH = min(maxL[i], maxR[i])
            diff = minH - height[i]
            if diff > 0:
                res += diff

        return res


# Solution: Two Pointers
# Calculating maxLeft and maxRight on the way and taking the minimum
# Substracting that with the current height will give us the rain water
# We also update the max also the pointer according if its left or right
# Very hard question
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        while l<r:
            if maxL > maxR:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
            else:
                l+= 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
        return res
        