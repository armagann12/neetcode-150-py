# Using sorting -> O(n logn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 0:
            return 0
        res = 1
        curr = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] + 1 == nums[i + 1]:
                curr += 1
            else:
                curr = 1
            res = max(res, curr)
        return res

#Using a Set -> O(n)
class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in numSet:
            print(n)
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                res = max(res, length)
        return res
