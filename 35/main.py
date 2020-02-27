class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        return l


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
