# My inital thought
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if arr[0] > target:
                continue
            if arr[-1] < target:
                continue
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return True

        return False
    
# You have to implement a binary search on a 2D matrix itself
# First binary search to select which array to use binary search
# My solution using a little help from neetcode theory part of the video
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = (high + low) // 2
            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                break
        l = 0
        r = len(matrix[mid]) - 1
        while l <= r:
            middle = (l + r) // 2
            if target > matrix[mid][middle]:
                l = middle + 1
            elif target < matrix[mid][middle]:
                r = middle - 1
            else: 
                return True
        return False