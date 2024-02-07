# My solution 
# Only Time limit exceeded not passed
# Looping throuhght array and using pointer for the rest of the array to see if it involves target
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if target < total:
                    r -= 1
                elif target > total:
                    l += 1
                else:
                    arr = [nums[i], nums[l], nums[r]]
                    # This part makes it time limit exceeded
                    if arr not in res:
                        res.append(arr)
                    l += 1
        return res

# Actual solution   
# Only differences is that if its duplicate it continues
# Also in neetcode it checks for < 0 and > 0

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # Only differences to my solution
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if target < total:
                    r -= 1
                elif target > total:
                    l += 1
                else:
                    arr = [nums[i], nums[l], nums[r]]
                    res.append(arr)
                    l += 1
                    # Only differences to my solution
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


# Using a hashmap
# Time limit exceeded but the same solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            hashMap = {}
            for j in range(i + 1, len(nums)):
                num = 0 - (nums[i] + nums[j])
                if num in hashMap:
                    arr = [nums[i], nums[j], num]
                    arr = sorted(arr)
                    # This part makes it time limit exceeded
                    if arr not in res:
                        res.append(arr)
                else:
                    hashMap[nums[j]] = 1
        return res