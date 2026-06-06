class Solution:
    nums: list[int]
    used: list[bool]
    path: list[int]
    result: list[list[int]]

    def __init__(self) -> None:
        self.nums = []
        self.used = []
        self.path = []
        self.result = []

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        self.nums = sorted(nums)
        self.used = [False] * len(nums)
        self.path = []
        self.result = []
        self.dfs()
        return self.result

    def dfs(self) -> None:
        if len(self.path) == len(self.nums):
            self.result.append(self.path.copy())
            return
        for i in range(len(self.nums)):
            if i > 0 and self.nums[i - 1] == self.nums[i] and not self.used[i - 1]:
                continue
            if self.used[i]:
                continue
            self.used[i] = True
            self.path.append(self.nums[i])
            self.dfs()
            self.used[i] = False
            self.path.pop()
