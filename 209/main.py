class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        j = 0
        sum = 0
        result = len(nums) + 1
        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                result = min(result, j - i + 1)
                sum -= nums[i]
                i += 1
            j += 1
        if result == len(nums) + 1:
            return 0
        return result
