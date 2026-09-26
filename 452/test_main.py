from main import Solution


def test_findMinArrowShots():
    s = Solution()
    assert s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert s.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
