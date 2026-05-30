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

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.used = [False] * len(nums)
        self.path = []
        self.result = []
        self.dfs()
        return self.result

    def dfs(self) -> None:
        if len(self.path) == len(self.nums):
            self.result.append(self.path.copy())
        for i in range(0, len(self.nums)):
            if self.used[i]:
                continue
            self.used[i] = True
            self.path.append(self.nums[i])
            self.dfs()
            self.used[i] = False
            self.path.pop()
