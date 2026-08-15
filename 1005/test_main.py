from main import Solution


def test_largestSumAfterKNegations():
    s = Solution()
    assert s.largestSumAfterKNegations([4, 2, 3], 1) == 5
    assert s.largestSumAfterKNegations([3, -1, 0, 2], 3) == 6
    assert s.largestSumAfterKNegations([2, -3, -1, 5, -4], 2) == 13
