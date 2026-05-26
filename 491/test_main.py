from main import Solution


def test_findSubsequences():
    s = Solution()
    assert s.findSubsequences([4, 6, 7, 7]) == [
        [4, 6],
        [4, 6, 7],
        [4, 6, 7, 7],
        [4, 7],
        [4, 7, 7],
        [6, 7],
        [6, 7, 7],
        [7, 7],
    ]
    assert s.findSubsequences([4, 4, 3, 2, 1]) == [[4, 4]]
