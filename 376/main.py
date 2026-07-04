class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        pre_diff = 0
        result = 1
        for i in range(0, len(nums) - 1):
            cur_diff = nums[i + 1] - nums[i]
            if (pre_diff >= 0 and cur_diff < 0) or (pre_diff <= 0 and cur_diff > 0):
                result += 1
                pre_diff = cur_diff
        return result
