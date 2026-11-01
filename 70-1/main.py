class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1, 2]
        sum = 0
        for _ in range(n - 2):
            sum = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = sum
        return sum
