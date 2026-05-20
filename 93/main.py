class Solution:
    result: list[str]

    def __init__(self) -> None:
        self.result = []

    def restoreIpAddresses(self, s: str) -> list[str]:
        self.result = []
        self.dfs(list(s), 0, 0)
        return self.result

    def dfs(self, s: list[str], start: int, count: int) -> None:
        if count == 3:
            if self.is_valid("".join(s[start : len(s)])):
                self.result.append("".join(s))
            return
        for i in range(start, len(s)):
            if self.is_valid("".join(s[start : i + 1])):
                s.insert(i + 1, ".")
                self.dfs(s, i + 2, count + 1)
                s.pop(i + 1)

    def is_valid(self, s: str) -> bool:
        if s == "":
            return False
        if s.startswith("0"):
            if len(s) == 1:
                return True
            else:
                return False
        else:
            if int(s) > 255:
                return False
            else:
                return True
