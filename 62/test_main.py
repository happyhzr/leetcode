from main import Solution


def test_uniquePaths():
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(7, 3) == 28
    assert s.uniquePaths(3, 3) == 6
