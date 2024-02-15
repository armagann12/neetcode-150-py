# Using a set
# I initally thought of using hashMap but because we care only if it exists or not
# we can use a set because we dont care about the number of times it exists
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        l = 0
        r = 1
        chars = set()
        chars.add(s[l])
        while r < len(s):
            if s[r] in chars:
                chars.remove(s[l])
                l += 1
            else:
                chars.add(s[r])
                r += 1
            res = max(res, r - l)
        return res


# Same solution but using a for loop for pointer r
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        chars = set()
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res
