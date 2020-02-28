class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        max = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            if dp[i-1] > 0:
                dp[i] += dp[i-1]
            if dp[i] > max:
                max = dp[i]
        return max


if __name__ == '__main__':
    s = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))
