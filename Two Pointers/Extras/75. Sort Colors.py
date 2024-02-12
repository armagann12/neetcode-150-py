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

# MergeSort


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

# Quicksort - Partition - Two Pass
# First loop swapping every 0 value to beginning
# Second loop swapping every 1 value from 0s


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tmp = nums[l]
                nums[l] = 0
                nums[i] = tmp
                l += 1
        for i in range(l, len(nums)):
            if nums[i] == 1:
                tmp = nums[l]
                nums[l] = 1
                nums[i] = tmp
                l += 1

# Quicksort - Partition - One pass - Two pointer
# This time using both left and right pointer for 0s and 2s
# To swap them to beggining and end of the array

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 2:
                tmp = nums[r]
                nums[r] = 2
                nums[i] = tmp
                r -= 1
                i -= 1
            elif nums[i] == 0:
                tmp = nums[l]
                nums[l] = 0
                nums[i] = tmp
                l += 1
            i += 1
