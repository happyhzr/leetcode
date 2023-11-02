from main import Solution


def test_main() -> None:
    s = Solution()
    res = s.letterCombinations("23")
    ans = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    for r in res:
        assert r in ans
    for a in ans:
        assert a in res

    res = s.letterCombinations("")
    ans = []
    for r in res:
        assert r in ans
    for a in ans:
        assert a in res

    res = s.letterCombinations("2")
    ans = ["a", "b", "c"]
    for r in res:
        assert r in ans
    for a in ans:
        assert a in res
