# Using Hashmap and sorting the hasmap by value and getting the keys [:k]
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    resMap = {}
    result = []
    for num in nums:
        resMap[num] = 1 + resMap.get(num, 0)

    resMap = dict(sorted(resMap.items(), key=lambda x: x[1], reverse=True))
    result = list(resMap.keys())[:k]
    return result
