from main import Solution


def test_sortedSquares():
    s = Solution()
    nums = [-4, -1, 0, 3, 10]
    result = s.sortedSquares(nums)
    assert result == [0, 1, 9, 16, 100]

    nums = [-7, -3, 2, 3, 11]
    result = s.sortedSquares(nums)
    assert result == [4, 9, 9, 49, 121]
