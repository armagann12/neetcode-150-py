# Time limit exceded
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        res = []
        while k + i <= len(nums):
            res.append(max(nums[i:k + i]))
            i += 1
        return res

# Time limit exceeded
# Using an extra array
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = nums[0:k]
        res = [max(arr)]
        i = 1
        while k + i <= len(nums):   
            arr.append(nums[k + i - 1])
            arr.pop(0)
            i += 1
            res.append(max(arr))
        return res
        