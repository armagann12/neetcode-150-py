# But this is n logn
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[a]
            a+= 1
        nums1.sort()

# Using an extra array
# Something like this but this doesnt work and needs refactoring but you get the solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = []
        l = 0
        r = 0
        len1 = len(nums1)
        len2 = len(nums2)
        while len(arr) < len(nums1):
            if nums1[l] == 0:
                arr = arr + nums2[r:]
            elif r == len2:
                arr = arr + nums1[l:]
            elif l == len1:
                arr = arr + nums2[r:]
            elif nums1[l] < nums2[r]:
                arr.append(nums1[l])
                l += 1
            else:
                arr.append(nums2[r])
                r += 1
        nums1 = arr

# Using two pointers on two different arrays
# starting from end of the nums1 and using m and n as pointers
# So we are using all end values
# Than we check which one is bigger and place in to that index
# If there is any nums left in nums2 than we place it in the index of nums1 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[i] = nums2[n - 1]
                n -= 1
            else:
                nums1[i] = nums1[m -1]
                m -= 1
            i -= 1
        while n> 0:
            nums1[i] = nums2[n - 1]
            n -= 1
            i-= 1


            


            
        