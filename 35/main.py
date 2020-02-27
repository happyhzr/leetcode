class Solution:
    def searchInsert(self, nums, target):
        for i, e in enumerate(nums):
            if e == target or e > target:
                return i
        return len(nums)


if __name__ == '__main__':
    s = Solution()

    nums = [1, 3, 5, 6]
    target = 5
    print(s.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 2
    print(s.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 7
    print(s.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 0
    print(s.searchInsert(nums, target))
