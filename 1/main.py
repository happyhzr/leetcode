class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)-1):
            another = target-nums[i]
            if another in hash and hash[another] != i:
                return [i, hash[another]]

        # nums.sort()
        # for i in range(len(nums)-1):
        #     another = target-nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == another:
        #             return [i, j]
        #         if nums[j] > another:
        #             break


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    ans = s.twoSum(nums, target)
    print(ans)
