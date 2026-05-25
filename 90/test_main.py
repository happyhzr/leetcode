from main import Solution


def test_subsetsWithDup() -> None:
    s = Solution()
    assert s.subsetsWithDup([1, 2, 2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert s.subsetsWithDup([0]) == [[], [0]]
