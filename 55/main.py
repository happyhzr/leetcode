class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        cover = 0
        i = 0
        while i <= cover:
            if i + nums[i] > cover:
                cover = i + nums[i]
            if (cover >= len(nums) - 1):
                return True
            i += 1
        return False
