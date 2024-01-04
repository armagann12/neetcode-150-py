# Initial though

def isAnagram(self, s, t):
    map = {}
    map2 = {}
    for letter in s:
        if letter in map:
            map[letter] += 1
        else:
            map[letter] = 1
    for letter in t:
        if letter in map2:
            map2[letter] += 1
        else:
            map2[letter] = 1
    return map == map2


# Refactored but same

def isAnagram(self, s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT
