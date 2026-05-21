class Solution:
    path: list[int]
    result: list[list[int]]
    nums: list[int]

    def __init__(self) -> None:
        self.path = []
        self.result = []
        self.nums = []

    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.path = []
        self.result = []
        self.nums = nums
        self.dfs(0)
        return self.result

    def dfs(self, start: int) -> None:
        self.result.append(self.path.copy())
        for i in range(start, len(self.nums)):
            self.path.append(self.nums[i])
            self.dfs(i + 1)
            self.path.pop()
