# Using sorting:

def groupAnagrams(self, strs):
    resMap = {}
    for string in strs:
        sortedString = "".join(sorted(string))
        if resMap.get(sortedString) == None:
            resMap[sortedString] = [string]
        else:
            resMap[sortedString].append(string)
    return resMap.values()
