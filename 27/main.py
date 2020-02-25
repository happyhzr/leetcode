class Solution:
    def removeElement(self, nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == '__main__':
    s = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    l = s.removeElement(nums)
    for i in range(l):
        print(nums[i], end=' ')
    print('\n')
