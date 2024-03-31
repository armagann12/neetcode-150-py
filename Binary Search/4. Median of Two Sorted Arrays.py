# Mergin arrays and sorting them and returning the median
# Not optimal solution need to the binary search one
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        mid = (len(nums3) - 1) // 2
        if len(nums3) % 2 == 1:
            return nums3[mid]
        
        return (nums3[mid] + nums3[mid + 1]) / 2
        