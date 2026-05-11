from main import Solution


def test_combinationSum3():
    s = Solution()
    assert s.combinationSum3(3, 7) == [[1, 2, 4]]
    assert s.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
