class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if nums[i] > 0 and nums[i] > target and target >= 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums[i] + nums[j] > 0 and nums[i] + nums[j] > target and target >= 0:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
