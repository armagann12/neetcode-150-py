# Same sliding window solution starting with l,r same position and incrementing r with a loop
# While calculating the windows len and keep track of occurences with hashmap
# Than if windows length - maxValue in hashmap is bigger than k than we increment l everytime
# We do this because lets say A is in str 3 times and string is length of 5 than there is only 2 other strings
# Than we can check if its bigger than k and if it is we make the window smaller
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars = {}
        l = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            maxVal = max(chars.values())
            while (r - l + 1) - maxVal > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
