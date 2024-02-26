# Sliding Window + hashmap
# My initial thought - not passed some test cases
# Basiclly created a count map of t and started to create a sliding window in s
# In that sliding window the first char hast to be in t and it compares everytime if the hashmaps are the same
# if not sliding window gets bigger If its the same it adds to the res array and left pointer + 1 so that it scans throught the array
# So basically we find every combination for that t and select the smallest one by comparing hashmaps
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        resMap = {}
        res = []
        for c in t:
            count[c] = count.get(c, 0) + 1
        l = 0
        r = 0
        while r < len(s) and l < len(s):
            if s[l] not in count:
                l+= 1
            else:
                if s[r] in count:
                    resMap[s[r]] = resMap.get(s[r], 0) + 1
                if resMap.keys() == count.keys() and 0 not in resMap.values() :
                    res.append(s[l:r + 1])
                    resMap[s[l]] -= 1
                    l += 1
                    resMap[s[r]] -= 1
                    r -= 1
                r += 1
        return min(res, key=len)
    