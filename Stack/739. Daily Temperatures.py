# Solution wihouth refactoring + Time limit exceeded
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
            
            
