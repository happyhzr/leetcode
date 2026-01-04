from main import Solution


def test_search():
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    ans = s.search(nums, 9)
    assert ans == 4

    nums = [-1, 0, 3, 5, 9, 12]
    ans = s.search(nums, 2)
    assert ans == -1
