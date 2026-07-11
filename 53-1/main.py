import sys


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = -sys.maxsize - 1
        count = 0
        for v in nums:
            count += v
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result
