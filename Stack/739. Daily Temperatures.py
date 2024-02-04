# Solution wihouth refactoring + Time limit exceeded
# With using hashmap
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            hashMap = {}
            temp = temperatures[i]
            hashMap[temp] = i
            if len(stack) != 0:
                for j in range(len(stack)):
                    mp = stack[-1]
                    keys = mp.keys()
                    # Refactor this for loop
                    for key in keys:
                        if temp > key:
                            stack.pop()
                            res[mp[key]] = i - mp[key]
            stack.append(hashMap)

        return res

# Time limit exceded     
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        indexes = []
        for i in range(len(temperatures)):
            temp = temperatures[i]

            if len(stack) != 0:
                for j in range(len(stack)):
                    if temp > stack[-1]:
                        el = stack.pop()
                        index = indexes.pop()
                        res[index] = i - index
            stack.append(temp)
            indexes.append(i)

        return res

# Accepted solution
# My solution
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        indexes = []
        for i in range(len(temperatures)):
            temp = temperatures[i]

            while len(stack) != 0 and temp > stack[-1]:
                el = stack.pop()
                index = indexes.pop()
                res[index] = i - index
            stack.append(temp)
            indexes.append(i)

        return res


# Refactored 
# Using only one list
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temp > stack[-1][0]:
                el = stack.pop()
                res[el[1]] = i - el[1]
            stack.append([temp, i])

        return res


