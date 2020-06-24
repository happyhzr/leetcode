class Solution:
    def singleNumber(self, nums):
        hash = {}
        for i in range(len(nums)):
            if not hash.get(nums[i]):
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1

        for k in hash:
            if hash[k] == 1:
                return k


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 1]
    print(s.singleNumber(nums))

    nums = [4, 1, 2, 1, 2]
    print(s.singleNumber(nums))
