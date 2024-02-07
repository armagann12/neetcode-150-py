# Hard question
# Its about finding ith elements left and right biggest elements min value and subtracting form the ith element


# Solution: Using extra arrays
# Calculating leftMax and rightMax values with two extra arrays
# Than taking min value of them and substracting from the element
# And that is the rain water being trapped
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