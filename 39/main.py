class Solution:
    candidates: list[int]
    path: list[int]
    result: list[list[int]]

    def __init__(self) -> None:
        self.candidates = []
        self.path = []
        self.result = []

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.candidates = sorted(candidates)
        self.path = []
        self.result = []
        self.dfs(target, 0)
        return self.result

    def dfs(self, target: int, start: int) -> None:
        if target == 0:
            self.result.append(self.path.copy())
            return
        for i in range(start, len(self.candidates)):
            if self.candidates[i] > target:
                break
            self.path.append(self.candidates[i])
            self.dfs(target - self.candidates[i], i)
            self.path.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
