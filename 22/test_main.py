from typing import List
from main import Solution


def test_main() -> None:
    s = Solution()
    ans = s.generateParenthesis(3)
    assert is_same(ans, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    ans = s.generateParenthesis(1)
    assert is_same(ans, ["()"])


def is_same(a: List[str], b: List[str]) -> None:
    for s1 in a:
        if s1 not in b:
            return False
    for s2 in b:
        if s2 not in a:
            return False
    return True
