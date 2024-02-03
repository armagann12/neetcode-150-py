class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if i == 0:
                stack.append(temperatures[i])
                continue

            if temperatures[i] > stack[-1]:
                stack.pop()
                res[i - 1] += 1
            # It should check if stack is empty or not if not it should check for > again
            stack.append(temperatures[i])
