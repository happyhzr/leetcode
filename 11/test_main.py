from main import Solution


def test_main():
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert s.maxArea(height) == 49
    height = [1, 1]
    assert s.maxArea(height) == 1
