from main import Solution


def test_intersection():
    s = Solution()
    result = s.intersection([1, 2, 2, 1], [2, 2])
    assert set(result) == set([2])
    result = s.intersection([4, 9, 5], [9, 4, 9, 8, 4])
    assert set(result) == set([9, 4])
