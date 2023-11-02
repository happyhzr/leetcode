from typing import List


class Solution:
    def __init__(self) -> None:
        self.table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        self._helper("", digits, res)
        return res

    def _helper(self, combination: str, digits: str, res: List[str]) -> None:
        if len(digits) == 0:
            res.append(combination)
        else:
            for c in self.table[digits[0]]:
                self._helper(combination + c, digits[1:], res)
