class Solution:
    path: list[int]
    result: list[list[int]]

    def __init__(self) -> None:
        self.path = []
        self.result = []

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        self.path = []
        self.result = []
        self.dfs(k, n, 1)
        return self.result

    def dfs(self, k: int, n: int, start: int) -> None:
        if n < 0:
            return
        if len(self.path) == k:
            if n == 0:
                self.result.append(self.path.copy())
            return
        for i in range(start, 9 - k + len(self.path) + 1 + 1):
            self.path.append(i)
            self.dfs(k, n - i, i + 1)
            self.path.pop()
