from main import Solution


def test_candy():
    s = Solution()
    assert s.candy([1, 0, 2]) == 5
    assert s.candy([1, 2, 2]) == 4
