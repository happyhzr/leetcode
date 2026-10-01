from main import Solution


def test_erase_overlap_intervals():
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
