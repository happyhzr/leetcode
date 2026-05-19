class Solution:
    s: str
    path: list[str]
    result: list[list[str]]

    def __init__(self) -> None:
        self.s = ""
        self.path = []
        self.result = []

    def partition(self, s: str) -> list[list[str]]:
        self.s = s
        self.path = []
        self.result = []
        self.dfs(0)
        return self.result

    def dfs(self, start: int) -> None:
        if start == len(self.s):
            self.result.append(self.path.copy())
            return
        for i in range(start, len(self.s)):
            if self.is_palindrome(self.s[start : i + 1]):
                self.path.append(self.s[start : i + 1])
            else:
                continue
            self.dfs(i + 1)
            self.path.pop()

    def is_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
