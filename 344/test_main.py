from main import Solution


def test_reverseString():
    s = Solution()
    lst = ["h", "e", "l", "l", "o"]
    s.reverseString(lst)
    assert lst == ["o", "l", "l", "e", "h"]
    lst = ["H", "a", "n", "n", "a", "h"]
    s.reverseString(lst)
    assert lst == [
        "h",
        "a",
        "n",
        "n",
        "a",
        "H",
    ]
