# Hard problem on my own
# Is it O(n) -> I think so beacuse we go through all of the hashmap and that hashmap is max n times isn't it?

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                hashMap[nums[i]] = 1
        res = 1
        while res in hashMap:
            res += 1
        return res
