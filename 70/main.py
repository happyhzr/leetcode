class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()

    n = 2
    print(s.climbStairs(n))

    n = 3
    print(s.climbStairs(n))
