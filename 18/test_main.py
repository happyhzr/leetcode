from main import Solution


def test_fourSum():
    s = Solution()
    assert s.fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]
    assert s.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert s.fourSum([], 0) == []
    assert s.fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
