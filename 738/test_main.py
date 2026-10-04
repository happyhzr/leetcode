from main import Solution


def test_monotone_increasing_digits():
    s = Solution()
    assert s.monotoneIncreasingDigits(10) == 9
    assert s.monotoneIncreasingDigits(1234) == 1234
    assert s.monotoneIncreasingDigits(332) == 299
