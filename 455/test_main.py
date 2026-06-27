from main import Solution


def test_findContentChildren():
    s = Solution()
    assert s.findContentChildren([1, 2, 3], [1, 1]) == 1
    assert s.findContentChildren([1, 2], [1, 2, 3]) == 2
