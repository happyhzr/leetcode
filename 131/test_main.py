from main import Solution


def test_partition():
    s = Solution()
    assert s.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert s.partition("a") == [["a"]]
