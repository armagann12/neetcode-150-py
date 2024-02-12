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

# MergeSort / Quicksort you can do


# Using BucketSort
# Because we know there is only 3 values
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}
        for num in nums:
            count[num] = count.get(num) + 1

        index = 0
        for c in count:
            nums[index: index + count[c]] = [c] * count[c]
            index += count[c]
