class Solution:
    path: list[int]
    result: list[list[int]]
    nums: list[int]
    used: list[bool]

    def __init__(self) -> None:
        self.path = []
        self.result = []
        self.nums = []
        self.used = []

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.path = []
        self.result = []
        self.nums = sorted(nums)
        self.used = [False] * len(nums)
        self.dfs(0)
        return self.result

    def dfs(self, start: int) -> None:
        self.result.append(self.path.copy())
        for i in range(start, len(self.nums)):
            if i > 0 and self.nums[i - 1] == self.nums[i] and not self.used[i - 1]:
                continue
            self.path.append(self.nums[i])
            self.used[i] = True
            self.dfs(i + 1)
            self.path.pop()
            self.used[i] = False
