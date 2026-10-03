from main import Solution


def test_merge():
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert s.merge([[4, 7], [1, 4]]) == [[1, 7]]
    assert s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
