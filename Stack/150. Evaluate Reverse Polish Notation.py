# Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        exp = ["+", "-", "/", "*"]
        for token in tokens:
            if token in exp:
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    third = first + second
                elif token == "-":
                    third = second - first
                elif token == "*":
                    third = first * second
                elif token == "/":
                    if first == 0 or second == 0:
                        third = 0
                    else:
                        third = int(second / first)
                stack.append(third)
            else:
                stack.append(int(token))
        return stack[0]
