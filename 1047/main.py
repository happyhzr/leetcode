class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)
