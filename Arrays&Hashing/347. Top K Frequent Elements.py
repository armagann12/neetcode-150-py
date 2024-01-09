# Using Hashmap and sorting the hasmap by value and getting the keys [:k]
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    resMap = {}
    result = []
    for num in nums:
        resMap[num] = 1 + resMap.get(num, 0)

    resMap = dict(sorted(resMap.items(), key=lambda x: x[1], reverse=True))
    result = list(resMap.keys())[:k]
    return result

# Using the hashmap like the first one but keys and values are reversed. Using sort of like bucket sort solution not sure
# Needs refactoring

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    nums = sorted(nums)
    count = 1
    resMap = {}
    result = []
    for i in range(len(nums)):
        if i == len(nums) - 1:
            if count not in resMap:
                resMap[count] = []
            resMap[count].append(nums[i])
        elif nums[i] == nums[i + 1]:
            count += 1
        else:
            if count not in resMap:
                resMap[count] = []
            resMap[count].append(nums[i])
            count = 1
    resultKeys = list(sorted(resMap.keys(), reverse=True))[:k]
    for keys in resultKeys:
        for key in resMap[keys]:
            result.append(key)
            k -= 1
            if k == 0:
                return result
    return result

# Refactored neetcode version also using an array

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for n, c in count.items():
        freq[c].append(n)

    result = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result




# You can also use heap

