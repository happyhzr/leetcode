from main import Solution


def test_fourSumCount():
    s = Solution()
    assert s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
    assert s.fourSumCount([0], [0], [0], [0]) == 1
