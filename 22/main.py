from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.n = 0

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.n = n
        self.dfs([], 0, 0)
        return self.ans

    def dfs(self, a: List[str], left: int, right: int) -> None:
        if len(a) == 2 * self.n:
            self.ans.append("".join(a))
            return
        if left < self.n:
            a.append("(")
            self.dfs(a, left + 1, right)
            a.pop()
        if right < left:
            a.append(")")
            self.dfs(a, left, right + 1)
            a.pop()
