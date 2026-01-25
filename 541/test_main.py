from main import Solution


def test_reverseStr():
    s = Solution()
    assert s.reverseStr("abcdefg", 2) == "bacdfeg"
    assert s.reverseStr("abcd", 2) == "bacd"
