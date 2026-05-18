class Solution:
    path: list[int]
    result: list[list[int]]
    candidates: list[int]
    used: list[bool]

    def __int__(self):
        self.path = []
        self.result = []
        self.candidates = []
        self.used = []

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.path = []
        self.result = []
        self.candidates = sorted(candidates)
        self.used = [False] * len(candidates)
        self.dfs(target, 0)
        return self.result

    def dfs(self, target: int, start: int) -> None:
        if target < 0:
            return
        if target == 0:
            self.result.append(self.path.copy())
            return
        for i in range(start, len(self.candidates)):
            if (
                i > start
                and self.candidates[i] == self.candidates[i - 1]
                and self.used[i - 1] == False
            ):
                continue
            self.path.append(self.candidates[i])
            self.used[i] = True
            self.dfs(target - self.candidates[i], i + 1)
            self.path.pop()
            self.used[i] = False
