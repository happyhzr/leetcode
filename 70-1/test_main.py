from main import Solution


def test_climbStairs():
    solution = Solution()
    assert solution.climbStairs(1) == 1
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
    assert solution.climbStairs(4) == 5
    assert solution.climbStairs(5) == 8
    assert solution.climbStairs(6) == 13
    assert solution.climbStairs(7) == 21
    assert solution.climbStairs(8) == 34
    assert solution.climbStairs(9) == 55
    assert solution.climbStairs(10) == 89
