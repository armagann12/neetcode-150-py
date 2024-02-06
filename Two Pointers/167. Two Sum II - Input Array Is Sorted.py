# Two Pointers without hashmap
# Time limit exceeded
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l < len(numbers) - 1:
            num = target - numbers[l]
            if num == numbers[r]:
                return [l + 1, r + 1]
            if num > numbers[r]:
                r += 1
            else:
                l += 1
                r = l + 1
            if r > len(numbers) - 1:
                l += 1
                r = l + 1
        return []

# Two Pointers correct solution
# From start to far end right

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
