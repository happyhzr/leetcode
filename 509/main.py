class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0, 1]
        sum = 0
        for _ in range(n - 1):
            sum = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = sum
        return sum
