class Solution:
    def jump(self, nums: list[int]) -> int:
        ans = 0
        cur = 0
        next = 0
        for i in range(len(nums) - 1):
            next = max(next, i + nums[i])
            if i == cur:
                ans += 1
                cur = next
        return ans
