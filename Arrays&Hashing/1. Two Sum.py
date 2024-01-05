def twoSum(self, nums, target):
    map = {}
    for i in range(len(nums)):
        if target - nums[i] in map:
            return [map[target - nums[i]], i]
        map[nums[i]] = i
    return []
