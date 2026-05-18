from main import Solution


def test_combinationSum2():
    s = Solution()
    assert s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6],
    ]
    assert s.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
