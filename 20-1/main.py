class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            elif len(stack) == 0:
                return False
            elif c != stack[-1]:
                return False
            else:
                stack.pop()
        return len(stack) == 0
