class Solution:
    nums: list[int]
    path: list[int]
    result: list[list[int]]

    def __init__(self) -> None:
        self.nums = []
        self.path = []
        self.result = []

    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.path = []
        self.result = []
        self.dfs(0)
        return self.result

    def dfs(self, start: int) -> None:
        if len(self.path) >= 2:
            self.result.append(self.path.copy())
        used = set()
        for i in range(start, len(self.nums)):
            if (
                len(self.path) != 0
                and self.nums[i] < self.path[-1]
                or self.nums[i] in used
            ):
                continue
            self.path.append(self.nums[i])
            used.add(self.nums[i])
            self.dfs(i + 1)
            self.path.pop()
