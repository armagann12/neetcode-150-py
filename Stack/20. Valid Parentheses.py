# Doing a if else solution with a loop


# Stack solution
class Solution:
    def isValid(self, s: str) -> bool:
        res = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        stack = []
        for c in s:
            if c == "[" or c ==  "(" or c == "{":
                stack.insert(0, c)
            else:
                if len(stack) == 0:
                    return False
                if c != res.get(stack[0]):
                    return False
                stack.pop(0)
        if len(stack) != 0:
            return False
        return True
    

# Refactored
class Solution:
    def isValid(self, s: str) -> bool:
        res = {"[": "]", "{": "}", "(": ")"}
        stack = []
        for c in s:
            if c in res:
                stack.append(c)
            elif len(stack) == 0 or c != res[stack.pop()]:
                return False
        return len(stack) == 0
