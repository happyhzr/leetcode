from main import Solution


def test_fib():
    s = Solution()
    assert s.fib(2) == 1
    assert s.fib(3) == 2
    assert s.fib(4) == 3
