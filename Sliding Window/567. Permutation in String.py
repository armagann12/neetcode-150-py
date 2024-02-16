# Important question because this is like comparing hashmaps

# My inital thought would be this
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for s in s1:
            count1[s] = count1.get(s, 0) + 1
        count2 = {}
        for s in s2:
            count2[s] = count2.get(s, 0) + 1
        return  # count2 contains count1 or not

# Importtant when doing sliding window you have to start from the beggining you cant do l = 0 r = 3
# because you have to calculate the between for that you need to start from beginning l = 0 r= 0 or 1

# TLE my solution can be refactored
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for s in s1:
            count[s] = count.get(s, 0) + 1
        l = 0
        while l < len(s2):
            if s2[l] in count:
                r = l + 1
                newCount = {}
                newCount[s2[l]] = 1
                while r < len(s2) and r <= l + len(s1) - 1 and s2[r] in count:
                    newCount[s2[r]] = newCount.get(s2[r], 0) + 1
                    r += 1
                if newCount == count:
                    return True
            l += 1

        return False

# Using sorting
# Checking every window in string that is length of s1
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if sorted(s1) == sorted(s2):
            return True
        s1 = sorted(s1)
        l = 0
        r = l + len(s1)
        while r < len(s2):
            r = l + len(s1)
            arr = s2[l:r]
            if sorted(arr) == s1:
                return True
            l += 1

        return False


# This is the actual thing
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = l + len(s1)
        while r < len(s2):
            r = l + len(s1)
            arr = s2[l:r]
            print(arr, s1, "is it a valid anagram")
            l += 1
        return False

        