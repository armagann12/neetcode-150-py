# Bubble Sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j + 1] < nums[j]:
                    tmp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = tmp

# My solution using hints
# Using Counting array - two pass solutio
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting Sort
        # An array as length of nums (3 for this question)
        # and indexes are the nums values are the occurences
        count = [0] * 3
        for num in nums:
            count[num] += 1

        start = 0
        for i in range(len(nums)):
            while count[start] == 0:
                start += 1
            nums[i] = start
            count[start] -= 1
