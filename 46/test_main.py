from main import Solution


def test_permute():
    s = Solution()
    assert s.permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert s.permute([0, 1]) == [[0, 1], [1, 0]]
    assert s.permute([1]) == [[1]]
