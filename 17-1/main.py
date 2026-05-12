class Solution:
    s: list[str]
    result: list[str]
    map: list[str]
    digits = ""

    def __init__(self) -> None:
        self.s = []
        self.result = []
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> list[str]:
        self.s = []
        self.result = []
        self.digits = digits
        self.dfs(0)
        return self.result

    def dfs(self, index: int) -> None:
        if index == len(self.digits):
            self.result.append("".join(self.s))
            return
        digit = int(self.digits[index])
        for letter in self.map[digit]:
            self.s.append(letter)
            self.dfs(index + 1)
            self.s.pop()
