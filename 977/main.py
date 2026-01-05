class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0 for _ in range(len(nums))]
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                result[k] = nums[i] * nums[i]
                k -= 1
                i += 1
            else:
                result[k] = nums[j] * nums[j]
                k -= 1
                j -= 1
        return result
