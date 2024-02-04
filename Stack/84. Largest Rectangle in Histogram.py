# Brute force solution
# Time limit exceeded

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = max(heights)

        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                minVal = min(heights[i:j + 1])
                area = minVal * (j-i + 1)
                res = max(res, area)
        return res


# Using two pointers
# This doesnt work needs refactoring and coding

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = 1
        while l < len(heights) - 1:
            minVal = min(heights[l:r + 1])
            area = minVal * (r-l + 1)
            print(minVal, area, l, r)

            if area >= res:
                res = max(res, area)
                if r < len(heights) - 1:
                    r += 1
                else:
                    l += 1
                    r = l + 1
            else:
                l = r
                r = l + 1

        return max(res, max(heights))


# Using stack?