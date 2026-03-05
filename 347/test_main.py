from main import Solution


def test_topKFrequent():
    s = Solution()
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    # assert s.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [1, 2]
