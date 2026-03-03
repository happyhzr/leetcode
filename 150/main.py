class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+" or c == "-" or c == "*" or c == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if c == "+":
                    stack.append(num2 + num1)
                elif c == "-":
                    stack.append(num2 - num1)
                elif c == "*":
                    stack.append(num2 * num1)
                else:
                    stack.append(num2 / num1)
            else:
                stack.append(c)
        result = int(stack.pop())
        return result
