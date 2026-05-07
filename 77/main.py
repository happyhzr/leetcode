class Solution:
    path: list[int]
    result: list[list[int]]

    def __init__(self) -> None:
        self.path = []
        self.result = []

    def combine(self, n: int, k: int) -> list[list[int]]:
        self.path = []
        self.result = []
        self.dfs(n, k, 1)
        return self.result

    def dfs(self, n: int, k: int, start: int) -> None:
        if len(self.path) + n - start + 1 < k:
            return
        if len(self.path) == k:
            self.result.append(self.path.copy())
            return
        for i in range(start, n + 1):
            self.path.append(i)
            self.dfs(n, k, i + 1)
            self.path.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
